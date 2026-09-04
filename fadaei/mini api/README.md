# mini api
Rahban Fleet API - FastAPI + JWT (by Amin Fadaei)

## Features
- User registration with mobile + national_id (roles: admin / user / company)
- JWT login via POST /token
- Vehicles by VIN, Devices by device_serial
- Activation only when VIN + National ID + Device Serial all exist
- A device cannot be active on two vehicles simultaneously
- POST /telemetry ingestion
- Role-based access control

## Run
Inside .APIvenv: uvicorn main:app --reload
Rahban Fleet mini api - FastAPI + JWT
