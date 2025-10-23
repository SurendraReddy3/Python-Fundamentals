from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.core.db import get_db
from app.schemas.cities import CityCreate, CityUpdate, CityPublic
from app.services.auth import get_current_user, require_role

router = APIRouter()

@router.get("/", dependencies=[Depends(get_current_user)])
async def list_cities(db=Depends(get_db)):
    items = []
    async for c in db.cities.find({}).sort("name"):
        items.append({"id": str(c["_id"]), "name": c.get("name"), "state": c.get("state"), "country": c.get("country")})
    return items

@router.post("/", dependencies=[Depends(require_role("admin"))], response_model=CityPublic)
async def create_city(payload: CityCreate, db=Depends(get_db)):
    res = await db.cities.insert_one(payload.model_dump())
    doc = await db.cities.find_one({"_id": res.inserted_id})
    return {"id": str(doc["_id"]), "name": doc.get("name"), "state": doc.get("state"), "country": doc.get("country")}

@router.get("/{city_id}", response_model=CityPublic)
async def get_city(city_id: str, db=Depends(get_db)):
    doc = await db.cities.find_one({"_id": ObjectId(city_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="City not found")
    return {"id": str(doc["_id"]), "name": doc.get("name"), "state": doc.get("state"), "country": doc.get("country")}

@router.patch("/{city_id}", dependencies=[Depends(require_role("admin"))], response_model=CityPublic)
async def update_city(city_id: str, payload: CityUpdate, db=Depends(get_db)):
    update = {k: v for k, v in payload.model_dump().items() if v is not None}
    await db.cities.update_one({"_id": ObjectId(city_id)}, {"$set": update})
    return await get_city(city_id, db)

@router.delete("/{city_id}", dependencies=[Depends(require_role("admin"))])
async def delete_city(city_id: str, db=Depends(get_db)):
    await db.cities.delete_one({"_id": ObjectId(city_id)})
    return {"status": "deleted"}
