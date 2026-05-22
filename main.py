from fastapi import FastAPI
from routes import router

app = FastAPI(title="Shipment Tracking Analytics Platform")

app.include_router(router)