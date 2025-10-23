from pydantic import BaseModel, Field
from typing import Optional

class CityCreate(BaseModel):
    name: str = Field(min_length=2)
    state: Optional[str] = None
    country: Optional[str] = None

class CityUpdate(BaseModel):
    name: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

class CityPublic(BaseModel):
    id: str
    name: str
    state: Optional[str] = None
    country: Optional[str] = None
