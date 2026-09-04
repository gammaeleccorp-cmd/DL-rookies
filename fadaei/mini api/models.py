from pydantic import BaseModel

# ---------- پایگاه داده موقت (داخل RAM) ----------
USERS = {}
VEHICLES = {}
DEVICES = {}
TELEMETRY = []

ALLOWED_ROLES = ["admin", "user", "company"]

# ---------- فرم‌های ورودی ----------
class UserCreate(BaseModel):
    username: str
    password: str
    mobile: str
    national_id: str
    role: str = "user"

class LoginRequest(BaseModel):
    username: str
    password: str

class VehicleCreate(BaseModel):
    vin: str
    model: str = "unknown"

class DeviceCreate(BaseModel):
    device_serial: str

class TelemetryCreate(BaseModel):
    device_serial: str
    speed: float = 0.0
    fuel: float = 0.0
