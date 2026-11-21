from datetime import datetime, timedelta
import jwt
from fastapi import APIRouter, Depends, HTTPException, Header
from models import USERS, ALLOWED_ROLES, UserCreate, LoginRequest

SECRET_KEY = "rahban-secret-key-change-in-production"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

def create_access_token(user: dict) -> str:
    payload = {
        "sub": user["username"],
        "role": user["role"],
        "national_id": user["national_id"],
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(authorization: str = Header(None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = USERS.get(payload.get("sub"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/users/register")
def register(form: UserCreate):
    if form.role not in ALLOWED_ROLES:
        raise HTTPException(status_code=400, detail="Invalid role")
    if form.username in USERS:
        raise HTTPException(status_code=400, detail="Username already exists")
    USERS[form.username] = {
        "username": form.username,
        "password": form.password,
        "mobile": form.mobile,
        "national_id": form.national_id,
        "role": form.role,
    }
    return {"message": "User registered", "role": form.role}

@router.post("/auth/login")
def login(form: LoginRequest):
    user = USERS.get(form.username)
    if not user or user["password"] != form.password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    return {"access_token": create_access_token(user), "token_type": "bearer"}

@router.get("/auth/me")
def me(user: dict = Depends(get_current_user)):
    return {k: v for k, v in user.items() if k != "password"}
