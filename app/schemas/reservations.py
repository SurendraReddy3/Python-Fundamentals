from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class ReservationCreate(BaseModel):
    lot_id: str
    slot_index: Optional[int] = None
    hold_minutes: int = Field(default=15, ge=5, le=120)

class ReservationPublic(BaseModel):
    id: str
    user_id: str
    lot_id: str
    slot_index: int
    status: Literal["held", "checked_in", "completed", "cancelled", "expired"]
    created_at: datetime
    updated_at: datetime
    price: Optional[float] = None
