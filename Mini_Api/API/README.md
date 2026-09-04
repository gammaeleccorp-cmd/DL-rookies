# mini api

Rahban fleet API - FastAPI + JWT (OAuth2 password flow)

## Roles
- admin: manage users (/admin/users)
- user: register own vehicles/devices, send telemetry
- company: view all vehicles/devices

## Features
- Register users with mobile + national_id
- Register vehicles with VIN, devices with device_serial
- Activation rule: VIN + national_id + device_serial required;
  a device can be active on only ONE vehicle at a time
- POST /telemetry for active device+vehicle pair

## Run
pip install fastapi uvicorn "python-jose[cryptography]" "passlib[bcrypt]"
uvicorn main:app --reload --port 8000
