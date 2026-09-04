from fastapi import APIRouter, Depends, HTTPException
from models import VEHICLES, DEVICES, VehicleCreate, DeviceCreate
from auth import get_current_user

router = APIRouter()

@router.post("/vehicles")
def register_vehicle(form: VehicleCreate, user: dict = Depends(get_current_user)):
    if form.vin in VEHICLES:
        raise HTTPException(status_code=400, detail="VIN already exists")
    VEHICLES[form.vin] = {
        "vin": form.vin,
        "model": form.model,
        "owner_national_id": user["national_id"],
        "active_device": None,
    }
    return VEHICLES[form.vin]

@router.post("/devices")
def register_device(form: DeviceCreate, user: dict = Depends(get_current_user)):
    if form.device_serial in DEVICES:
        raise HTTPException(status_code=400, detail="Device serial already exists")
    DEVICES[form.device_serial] = {
        "device_serial": form.device_serial,
        "owner_username": user.get("username") or user.get("sub"),
        "owner_national_id": user.get("national_id"),
        "active_vin": None,
    }
    return DEVICES[form.device_serial]

@router.post("/devices/{serial}/activate/{vin}")
def activate_device(serial: str, vin: str, user: dict = Depends(get_current_user)):
    # قانون : VIN و سریال دستگاه باید وجود داشته باشند
    if vin not in VEHICLES:
        raise HTTPException(status_code=404, detail="VIN not found")
    if serial not in DEVICES:
        raise HTTPException(status_code=404, detail="Device not found")
    vehicle = VEHICLES[vin]
    device = DEVICES[serial]
    # قانون : فقط مالک خودرو (کد ملی) یا admin می‌تواند فعال‌سازی کند
    if user["role"] != "admin" and vehicle["owner_national_id"] != user["national_id"]:
        raise HTTPException(status_code=403, detail="You are not the owner of this vehicle")
    # قانون : یک دستگاه همزمان روی دو خودرو فعال نباشد
    if device["active_vin"] is not None and device["active_vin"] != vin:
        raise HTTPException(status_code=400, detail="Device is already active on another vehicle")
    device["active_vin"] = vin
    vehicle["active_device"] = serial
    return {"message": "Device activated", "device": serial, "vehicle": vin}

@router.get("/vehicles/me")
def get_my_vehicles(user: dict = Depends(get_current_user)):
    return [
        v for v in VEHICLES.values()
        if v.get("owner_national_id") == user.get("national_id")
    ]

@router.get("/devices/me")
def get_my_devices(user: dict = Depends(get_current_user)):
    my_username = user.get("username") or user.get("sub")
    return [
        d for d in DEVICES.values()
        if d.get("owner_username") == my_username
        or d.get("owner_national_id") == user.get("national_id")
    ]
