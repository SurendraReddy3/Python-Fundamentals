from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.core.db import get_db
from app.schemas.lots import LotCreate, LotUpdate, LotPublic
from app.services.auth import get_current_user, require_role
from app.routers.realtime import manager

router = APIRouter()

async def _serialize_lot(doc):
    occupied = doc.get("occupied_slots", 0)
    held = doc.get("held_slots", 0)
    total = doc.get("total_slots", 0)
    available = max(0, total - occupied - held)
    return {
        "id": str(doc["_id"]),
        "city_id": str(doc.get("city_id")),
        "name": doc.get("name"),
        "address": doc.get("address"),
        "total_slots": total,
        "available_slots": available,
        "pricing_per_hour": doc.get("pricing_per_hour", 0.0),
        "latitude": doc.get("latitude"),
        "longitude": doc.get("longitude"),
    }

@router.get("/", dependencies=[Depends(get_current_user)])
async def list_lots(city_id: str | None = None, db=Depends(get_db)):
    query = {"city_id": ObjectId(city_id)} if city_id else {}
    items = []
    async for doc in db.lots.find(query).sort("name"):
        items.append(await _serialize_lot(doc))
    return items

@router.post("/", dependencies=[Depends(require_role("admin"))], response_model=LotPublic)
async def create_lot(payload: LotCreate, db=Depends(get_db)):
    if not await db.cities.find_one({"_id": ObjectId(payload.city_id)}):
        raise HTTPException(status_code=400, detail="Invalid city")
    doc = payload.model_dump()
    doc["city_id"] = ObjectId(doc["city_id"])  # store as ObjectId
    doc.update({"occupied_slots": 0, "held_slots": 0})
    res = await db.lots.insert_one(doc)
    created = await db.lots.find_one({"_id": res.inserted_id})
    data = await _serialize_lot(created)
    await manager.broadcast_city(str(created["city_id"]), {"type": "lot_added", "lot": data})
    return data

@router.get("/{lot_id}", response_model=LotPublic)
async def get_lot(lot_id: str, db=Depends(get_db)):
    doc = await db.lots.find_one({"_id": ObjectId(lot_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Lot not found")
    return await _serialize_lot(doc)

@router.patch("/{lot_id}", dependencies=[Depends(require_role("admin"))])
async def update_lot(lot_id: str, payload: LotUpdate, db=Depends(get_db)):
    update = {k: v for k, v in payload.model_dump().items() if v is not None}
    await db.lots.update_one({"_id": ObjectId(lot_id)}, {"$set": update})
    data = await get_lot(lot_id, db)
    await manager.broadcast_lot(lot_id, {"type": "lot_update"})
    return data

@router.delete("/{lot_id}", dependencies=[Depends(require_role("admin"))])
async def delete_lot(lot_id: str, db=Depends(get_db)):
    await db.lots.delete_one({"_id": ObjectId(lot_id)})
    await manager.broadcast_lot(lot_id, {"type": "lot_deleted"})
    return {"status": "deleted"}
