from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.users import UserCreate, TokenResponse, UserPublic
from app.core.db import get_db
from app.services.auth import authenticate_user, create_user, issue_token_for_user
from app.services.auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserPublic)
async def register(payload: UserCreate, db=Depends(get_db)):
    user = await create_user(payload.email, payload.password, payload.full_name, role="user", db=db)
    return {"id": user["id"], "email": user["email"], "full_name": user.get("full_name"), "role": user.get("role", "user")}

@router.post("/login", response_model=TokenResponse)
async def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = await authenticate_user(form.username, form.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = await issue_token_for_user(user["id"], extra={"role": user.get("role", "user")})
    return TokenResponse(access_token=token)

@router.get("/me", response_model=UserPublic)
async def me(user=Depends(get_current_user)):
    return {"id": str(user["_id"]), "email": user.get("email"), "full_name": user.get("full_name"), "role": user.get("role", "user")}
