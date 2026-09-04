from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException

from models import (
    users_db, vehicles_db, devices_db, telemetry_db,
    UserRegister, UserLogin, VehicleCreate, DeviceCreate, TelemetryCreate,
)
from security import hash_password, create_access_token, get_current_user, require_role

router = APIRouter()


# ---------------- Users & Auth ----------------

@router.post("/users/register")
def register(body: UserRegister):
    if body.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    if body.role not in ("user", "admin", "company"):
        raise HTTPException(status_code=400, detail="Invalid role")
    users_db[body.username] = {
        "username": body.username,
        "password_hash": hash_password(body.password),
        "mobile": body.mobile,
        "national_id": body.national_id,
        "role": body.role,
    }
    return {"message": "User registered", "role": body.role}


@router.post("/auth/login")
def login(body: UserLogin):
    user = users_db.get(body.username)
    if not user or user["password_hash"] != hash_password(body.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/auth/me")
def me(user: dict = Depends(get_current_user)):
    return {k: v for k, v in user.items() if k != "password_hash"}


# ---------------- Admin / Company ----------------

@router.get("/admin/users")
def admin_users(user: dict = Depends(require_role("admin"))):
    return [{k: v for k, v in u.items() if k != "password_hash"} for u in users_db.values()]


@router.get("/admin/vehicles")
def admin_vehicles(user: dict = Depends(require_role("admin", "company"))):
    return list(vehicles_db.values())


@router.get("/admin/devices")   # NEW
def admin_devices(user: dict = Depends(require_role("admin", "company"))):
    return list(devices_db.values())


# ---------------- Vehicles ----------------

@router.post("/vehicles")
def create_vehicle(body: VehicleCreate, user: dict = Depends(get_current_user)):
    if body.vin in vehicles_db:
        raise HTTPException(status_code=400, detail="VIN already registered")
    vehicles_db[body.vin] = {
        "vin": body.vin,
        "model": body.model,
        "owner_national_id": user["national_id"],
        "active_device": None,
    }
    return vehicles_db[body.vin]


@router.get("/vehicles/me")   # NEW
def my_vehicles(user: dict = Depends(get_current_user)):
    return [v for v in vehicles_db.values() if v["owner_national_id"] == user["national_id"]]


# ---------------- Devices ----------------

@router.post("/devices")
def create_device(body: DeviceCreate, user: dict = Depends(get_current_user)):
    if body.device_serial in devices_db:
        raise HTTPException(status_code=400, detail="Device already registered")
    devices_db[body.device_serial] = {
        "device_serial": body.device_serial,
        "owner_national_id": user["national_id"],
        "active_vin": None,
    }
    return devices_db[body.device_serial]


@router.get("/devices/me")   # NEW
def my_devices(user: dict = Depends(get_current_user)):
    return [d for d in devices_db.values() if d["owner_national_id"] == user["national_id"]]


@router.post("/devices/{serial}/activate/{vin}")
def activate_device(serial: str, vin: str, user: dict = Depends(get_current_user)):
    device = devices_db.get(serial)
    vehicle = vehicles_db.get(vin)
    if not device or not vehicle:
        raise HTTPException(status_code=404, detail="Device or vehicle not found")
    if vehicle["owner_national_id"] != user["national_id"]:
        raise HTTPException(status_code=403, detail="You are not the owner of this vehicle")

    # LAW: a device must not be active on two vehicles simultaneously
    if device["active_vin"] is not None and device["active_vin"] != vin:
        raise HTTPException(status_code=409, detail="Device is already active on another vehicle")

    # LAW: a vehicle must not hold two active devices (data consistency)
    if vehicle["active_device"] is not None and vehicle["active_device"] != serial:
        raise HTTPException(status_code=409, detail="Vehicle already has an active device")

    device["active_vin"] = vin
    vehicle["active_device"] = serial
    return {"message": "Device activated", "device": serial, "vehicle": vin}


@router.post("/devices/{serial}/deactivate")   # NEW
def deactivate_device(serial: str, user: dict = Depends(get_current_user)):
    device = devices_db.get(serial)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    is_owner = device["owner_national_id"] == user["national_id"]
    is_admin = user["role"] == "admin"
    if not (is_owner or is_admin):
        raise HTTPException(status_code=403, detail="Only owner or admin can deactivate")

    if device["active_vin"] is None:
        raise HTTPException(status_code=400, detail="Device is not active")

    vehicle = vehicles_db.get(device["active_vin"])
    if vehicle and vehicle["active_device"] == serial:
        vehicle["active_device"] = None
    device["active_vin"] = None
    return {"message": "Device deactivated", "device": serial}


# ---------------- Telemetry ----------------

@router.post("/telemetry")
def send_telemetry(body: TelemetryCreate, user: dict = Depends(get_current_user)):
    device = devices_db.get(body.device_serial)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if device["active_vin"] is None:
        raise HTTPException(status_code=400, detail="Device is not active on any vehicle")

    record = {
        "device_serial": body.device_serial,
        "vin": device["active_vin"],
        "speed": body.speed,
        "fuel": body.fuel,
        "timestamp": datetime.now().isoformat(),
    }
    telemetry_db.append(record)
    return {"message": "Telemetry received", "record": record}


@router.get("/telemetry")
def get_telemetry(user: dict = Depends(get_current_user)):
    if user["role"] in ("admin", "company"):
        return telemetry_db
    my_vins = {v["vin"] for v in vehicles_db.values() if v["owner_national_id"] == user["national_id"]}
    return [t for t in telemetry_db if t["vin"] in my_vins]

@router.get("/vehicles/me")
def get_my_vehicles(current_user: User = Depends(get_current_user)):
    return [v for v in VEHICLES.values() if v.owner_national_id == current_user.national_id]

@router.get("/devices/me")
def get_my_devices(current_user: User = Depends(get_current_user)):
    return [d for d in DEVICES.values() if d.owner_username == current_user.username]

@router.get("/vehicles/me")
def get_my_vehicles(current_user: User = Depends(get_current_user)):
    return [v for v in VEHICLES.values() if v.owner_national_id == current_user.national_id]

@router.get("/devices/me")
def get_my_devices(current_user: User = Depends(get_current_user)):
    return [d for d in DEVICES.values() if d.owner_username == current_user.username]
