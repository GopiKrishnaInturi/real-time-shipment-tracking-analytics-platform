import random
from database import SessionLocal
from models import Shipment

db = SessionLocal()

for i in range(100):
    shipment = Shipment(
        tracking_number=f"TRK{i}",
        status=random.choice(["IN_TRANSIT", "DELIVERED", "DELAYED"]),
        source="New York",
        destination="Dallas"
    )
    db.add(shipment)

db.commit()

print("Sample data inserted")