from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.routers import auth, cities, lots, reservations, realtime
from app.core.config import settings
from app.services.background import startup_tasks

app = FastAPI(title="Smart Parking Finder", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(cities.router, prefix="/api/cities", tags=["cities"])
app.include_router(lots.router, prefix="/api/lots", tags=["lots"])
app.include_router(reservations.router, prefix="/api/reservations", tags=["reservations"])
app.include_router(realtime.router, prefix="/api/realtime", tags=["realtime"])

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.on_event("startup")
async def _startup():
    await startup_tasks(app)
