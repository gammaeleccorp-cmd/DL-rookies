from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    password: str
    mobile: str
    national_id: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserOut(BaseModel):
    username: str
    mobile: str
    national_id: str


class DeviceRegister(BaseModel):
    device_serial: str


class VehicleRegister(BaseModel):
    vin: str
    owner_national_id: str


class ActivateRequest(BaseModel):
    vin: str
    national_id: str
    device_serial: str


class TelemetryPayload(BaseModel):
    device_serial: str
    speed: float
    lat: float
    lon: float
