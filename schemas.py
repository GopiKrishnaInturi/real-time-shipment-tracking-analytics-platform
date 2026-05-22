from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    tracking_number: str
    status: str
    source: str
    destination: str

class EventCreate(BaseModel):
    tracking_number: str
    event_type: str
    location: str