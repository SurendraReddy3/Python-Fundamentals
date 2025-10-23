from datetime import datetime, timezone
from fastapi import FastAPI
from asyncio import sleep, create_task
from bson import ObjectId

from app.core.db import get_db
from app.routers.realtime import manager
from app.services.bootstrap import ensure_admin

RUNNING = False

async def expiry_worker():
    global RUNNING
    if RUNNING:
        return
    RUNNING = True
    db = await get_db()
    while True:
        now = datetime.now(timezone.utc)
        # Expire held reservations
        cursor = db.reservations.find({"status": "held", "expires_at": {"$lte": now}})
        async for doc in cursor:
            await db.reservations.update_one({"_id": doc["_id"]}, {"$set": {"status": "expired", "updated_at": now}})
            await db.lots.update_one({"_id": doc["lot_id"]}, {"$inc": {"held_slots": -1}})
            await manager.broadcast_lot(str(doc["lot_id"]), {"type": "lot_update"})
        await sleep(30)

async def setup_indexes():
    db = await get_db()
    await db.users.create_index("email", unique=True)
    await db.cities.create_index("name")
    await db.lots.create_index([("city_id", 1), ("name", 1)])
    await db.reservations.create_index([("user_id", 1), ("status", 1)])
    await db.reservations.create_index("expires_at")

async def startup_tasks(app: FastAPI):
    await setup_indexes()
    await ensure_admin()
    create_task(expiry_worker())
