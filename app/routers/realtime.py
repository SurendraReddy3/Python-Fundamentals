from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from bson import ObjectId
from collections import defaultdict

from app.core.db import get_db

router = APIRouter()

class ConnectionManager:
    def __init__(self) -> None:
        self.city_channels: dict[str, set[WebSocket]] = defaultdict(set)
        self.lot_channels: dict[str, set[WebSocket]] = defaultdict(set)

    async def connect_city(self, city_id: str, websocket: WebSocket):
        await websocket.accept()
        self.city_channels[city_id].add(websocket)

    async def connect_lot(self, lot_id: str, websocket: WebSocket):
        await websocket.accept()
        self.lot_channels[lot_id].add(websocket)

    def disconnect(self, websocket: WebSocket):
        for channel in list(self.city_channels.values()):
            channel.discard(websocket)
        for channel in list(self.lot_channels.values()):
            channel.discard(websocket)

    async def broadcast_city(self, city_id: str, message: dict):
        for ws in list(self.city_channels.get(city_id, [])):
            await ws.send_json(message)

    async def broadcast_lot(self, lot_id: str, message: dict):
        for ws in list(self.lot_channels.get(lot_id, [])):
            await ws.send_json(message)

manager = ConnectionManager()

@router.websocket("/cities/{city_id}")
async def ws_city(websocket: WebSocket, city_id: str, db=Depends(get_db)):
    await manager.connect_city(city_id, websocket)
    try:
        while True:
            await websocket.receive_text()  # keep alive, ignore content
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@router.websocket("/lots/{lot_id}")
async def ws_lot(websocket: WebSocket, lot_id: str, db=Depends(get_db)):
    await manager.connect_lot(lot_id, websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
