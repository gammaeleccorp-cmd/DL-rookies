from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from models import TELEMETRY, DEVICES, VEHICLES, TelemetryCreate
from auth import get_current_user

router = APIRouter()

@router.post("/telemetry")
def send_telemetry(form: TelemetryCreate, user: dict = Depends(get_current_user)):
    device = DEVICES.get(form.device_serial)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    if device["active_vin"] is None:
        raise HTTPException(status_code=400, detail="Device is not active on any vehicle")
    record = {
        "device_serial": form.device_serial,
        "vin": device["active_vin"],
        "speed": form.speed,
        "fuel": form.fuel,
        "timestamp": datetime.utcnow().isoformat(),
    }
    TELEMETRY.append(record)
    return {"message": "Telemetry received", "record": record}

@router.get("/telemetry")
def get_telemetry(user: dict = Depends(get_current_user)):
    # admin و company کل ناوگان را می‌بینند، کاربر عادی فقط خودروهای خودش را
    if user["role"] in ("admin", "company"):
        return TELEMETRY
    my_vins = [v["vin"] for v in VEHICLES.values()
               if v["owner_national_id"] == user["national_id"]]
    return [t for t in TELEMETRY if t["vin"] in my_vins]
