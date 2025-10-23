from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from bson import ObjectId

from app.core.db import get_db
from app.core.security import verify_password, hash_password, create_access_token, decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    user["id"] = str(user["_id"])  # normalize
    return user

async def require_role(role: str):
    async def _guard(user=Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return _guard

async def authenticate_user(email: str, password: str, db):
    user = await db.users.find_one({"email": email})
    if not user:
        return None
    if not verify_password(password, user.get("password_hash", "")):
        return None
    user["id"] = str(user["_id"])  # normalize
    return user

async def create_user(email: str, password: str, full_name: Optional[str], role: str, db):
    existing = await db.users.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    password_hash = hash_password(password)
    doc = {"email": email, "password_hash": password_hash, "full_name": full_name, "role": role}
    res = await db.users.insert_one(doc)
    return {"id": str(res.inserted_id), **doc}

async def issue_token_for_user(user_id: str, extra: Optional[dict] = None):
    return create_access_token(user_id, extra=extra)
