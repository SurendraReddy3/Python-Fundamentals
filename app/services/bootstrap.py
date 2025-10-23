from app.core.config import settings
from app.core.db import get_db
from app.services.auth import create_user

async def ensure_admin():
    if not settings.admin_email or not settings.admin_password:
        return
    db = await get_db()
    existing = await db.users.find_one({"email": settings.admin_email})
    if not existing:
        await create_user(settings.admin_email, settings.admin_password, full_name="Admin", role="admin", db=db)
