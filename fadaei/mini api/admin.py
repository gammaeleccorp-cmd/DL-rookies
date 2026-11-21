from fastapi import APIRouter, Depends, HTTPException
from models import USERS, VEHICLES, DEVICES
from auth import get_current_user

router = APIRouter()

def require_role(*roles):
    # نگهبان تخصصی: فقط برچسب‌های داخل لیست roles اجازه ورود دارند
    def checker(user: dict = Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Access denied: role not allowed")
        return user
    return checker

@router.get("/admin/users")
def list_users(user: dict = Depends(require_role("admin"))):
    return [{k: v for k, v in u.items() if k != "password"} for u in USERS.values()]

@router.get("/admin/vehicles")
def list_vehicles(user: dict = Depends(require_role("admin", "company"))):
    return list(VEHICLES.values())

@router.get("/admin/devices")
def list_devices(user: dict = Depends(require_role("admin", "company"))):
    return list(DEVICES.values())
