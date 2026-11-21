from fastapi import FastAPI
import auth, vehicles, telemetry, admin

app = FastAPI(title="Rahban API")

app.include_router(auth.router)
app.include_router(vehicles.router)
app.include_router(telemetry.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Rahban API is running"}
