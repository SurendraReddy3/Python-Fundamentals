from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from datetime import datetime, timedelta, timezone

from app.core.db import get_db
from app.schemas.reservations import ReservationCreate, ReservationPublic
from app.services.auth import get_current_user
from app.routers.realtime import manager

router = APIRouter()

HOLD_PREFIX = "hold:"  # key prefix for held slots

async def _get_available_slot(db, lot_id: ObjectId) -> int | None:
    lot = await db.lots.find_one({"_id": lot_id})
    if not lot:
        return None
    total = lot.get("total_slots", 0)
    occupied = lot.get("occupied_slots", 0)
    held = lot.get("held_slots", 0)
    available = total - occupied - held
    if available <= 0:
        return None
    # Simple strategy: next free index is occupied+held
    return occupied + held

@router.post("/", response_model=ReservationPublic)
async def create_reservation(payload: ReservationCreate, user=Depends(get_current_user), db=Depends(get_db)):
    lot_id = ObjectId(payload.lot_id)
    lot_doc = await db.lots.find_one({"_id": lot_id})
    if not lot_doc:
        raise HTTPException(status_code=400, detail="Invalid lot")

    slot_index = payload.slot_index
    if slot_index is None:
        slot_index = await _get_available_slot(db, lot_id)
        if slot_index is None:
            raise HTTPException(status_code=409, detail="No available slots")

    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(minutes=payload.hold_minutes)
    res_doc = {
        "user_id": ObjectId(user["_id"]),
        "lot_id": lot_id,
        "slot_index": slot_index,
        "status": "held",
        "created_at": now,
        "updated_at": now,
        "expires_at": expires_at,
        "price": None,
    }
    insert = await db.reservations.insert_one(res_doc)
    await db.lots.update_one({"_id": lot_id}, {"$inc": {"held_slots": 1}})
    await manager.broadcast_lot(str(lot_id), {"type": "lot_update"})
    await manager.broadcast_city(str(lot_doc["city_id"]), {"type": "lot_update"})
    doc = await db.reservations.find_one({"_id": insert.inserted_id})
    return {
        "id": str(doc["_id"]),
        "user_id": str(doc["user_id"]),
        "lot_id": str(doc["lot_id"]),
        "slot_index": doc["slot_index"],
        "status": doc["status"],
        "created_at": doc["created_at"],
        "updated_at": doc["updated_at"],
        "price": doc.get("price"),
    }

@router.post("/{reservation_id}/checkin", response_model=ReservationPublic)
async def checkin(reservation_id: str, user=Depends(get_current_user), db=Depends(get_db)):
    _id = ObjectId(reservation_id)
    doc = await db.reservations.find_one({"_id": _id, "user_id": ObjectId(user["_id"])})
    if not doc or doc.get("status") != "held":
        raise HTTPException(status_code=400, detail="Invalid reservation")
    now = datetime.now(timezone.utc)
    await db.reservations.update_one({"_id": _id}, {"$set": {"status": "checked_in", "updated_at": now, "checkin_at": now}})
    await db.lots.update_one({"_id": doc["lot_id"]}, {"$inc": {"held_slots": -1, "occupied_slots": 1}})
    lot_doc = await db.lots.find_one({"_id": doc["lot_id"]})
    await manager.broadcast_lot(str(doc["lot_id"]), {"type": "lot_update"})
    if lot_doc:
        await manager.broadcast_city(str(lot_doc["city_id"]), {"type": "lot_update"})
    new_doc = await db.reservations.find_one({"_id": _id})
    return {
        "id": str(new_doc["_id"]),
        "user_id": str(new_doc["user_id"]),
        "lot_id": str(new_doc["lot_id"]),
        "slot_index": new_doc["slot_index"],
        "status": new_doc["status"],
        "created_at": new_doc["created_at"],
        "updated_at": new_doc["updated_at"],
        "price": new_doc.get("price"),
    }

@router.post("/{reservation_id}/checkout", response_model=ReservationPublic)
async def checkout(reservation_id: str, user=Depends(get_current_user), db=Depends(get_db)):
    _id = ObjectId(reservation_id)
    doc = await db.reservations.find_one({"_id": _id, "user_id": ObjectId(user["_id"])})
    if not doc or doc.get("status") != "checked_in":
        raise HTTPException(status_code=400, detail="Invalid reservation state")
    now = datetime.now(timezone.utc)
    lot = await db.lots.find_one({"_id": doc["lot_id"]})
    checkin_at = doc.get("checkin_at", now)
    hours = max(1.0, (now - checkin_at).total_seconds() / 3600.0)
    price = round(hours * float(lot.get("pricing_per_hour", 0.0)), 2)

    await db.reservations.update_one({"_id": _id}, {"$set": {"status": "completed", "updated_at": now, "checkout_at": now, "price": price}})
    await db.lots.update_one({"_id": doc["lot_id"]}, {"$inc": {"occupied_slots": -1}})
    await manager.broadcast_lot(str(doc["lot_id"]), {"type": "lot_update"})
    if lot:
        await manager.broadcast_city(str(lot["city_id"]), {"type": "lot_update"})

    new_doc = await db.reservations.find_one({"_id": _id})
    return {
        "id": str(new_doc["_id"]),
        "user_id": str(new_doc["user_id"]),
        "lot_id": str(new_doc["lot_id"]),
        "slot_index": new_doc["slot_index"],
        "status": new_doc["status"],
        "created_at": new_doc["created_at"],
        "updated_at": new_doc["updated_at"],
        "price": new_doc.get("price"),
    }

@router.post("/{reservation_id}/cancel", response_model=ReservationPublic)
async def cancel(reservation_id: str, user=Depends(get_current_user), db=Depends(get_db)):
    _id = ObjectId(reservation_id)
    doc = await db.reservations.find_one({"_id": _id, "user_id": ObjectId(user["_id"])})
    if not doc or doc.get("status") not in {"held", "checked_in"}:
        raise HTTPException(status_code=400, detail="Invalid reservation state")
    now = datetime.now(timezone.utc)
    inc = {"held_slots": -1} if doc.get("status") == "held" else {"occupied_slots": -1}
    await db.reservations.update_one({"_id": _id}, {"$set": {"status": "cancelled", "updated_at": now}})
    await db.lots.update_one({"_id": doc["lot_id"]}, {"$inc": inc})
    lot_doc = await db.lots.find_one({"_id": doc["lot_id"]})
    await manager.broadcast_lot(str(doc["lot_id"]), {"type": "lot_update"})
    if lot_doc:
        await manager.broadcast_city(str(lot_doc["city_id"]), {"type": "lot_update"})

    new_doc = await db.reservations.find_one({"_id": _id})
    return {
        "id": str(new_doc["_id"]),
        "user_id": str(new_doc["user_id"]),
        "lot_id": str(new_doc["lot_id"]),
        "slot_index": new_doc["slot_index"],
        "status": new_doc["status"],
        "created_at": new_doc["created_at"],
        "updated_at": new_doc["updated_at"],
        "price": new_doc.get("price"),
    }
