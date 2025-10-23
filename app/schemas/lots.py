from pydantic import BaseModel, Field
from typing import Optional, Literal

class LotCreate(BaseModel):
    city_id: str
    name: str
    address: str
    total_slots: int = Field(ge=1)
    pricing_per_hour: float = Field(ge=0)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class LotUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    total_slots: Optional[int] = Field(default=None, ge=1)
    pricing_per_hour: Optional[float] = Field(default=None, ge=0)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class Slot(BaseModel):
    index: int
    status: Literal["free", "held", "occupied"]

class LotPublic(BaseModel):
    id: str
    city_id: str
    name: str
    address: str
    total_slots: int
    available_slots: int
    pricing_per_hour: float
    latitude: Optional[float] = None
    longitude: Optional[float] = None
