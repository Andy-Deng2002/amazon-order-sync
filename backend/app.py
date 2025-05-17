from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from models import Order, SessionLocal, engine, Base
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderSchema(BaseModel):
    order_id: str
    status: str
    order_time: str
    purchase_time: Optional[str] = None
    ship_time: Optional[str] = None
    arrival_time: Optional[str] = None
    amazon_estimated_arrival_time: Optional[str] = None

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/orders", response_model=List[OrderSchema])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@app.post("/orders", response_model=OrderSchema)
def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.put("/orders/{order_id}", response_model=OrderSchema)
def update_order(order_id: str, order: OrderSchema, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for key, value in order.dict().items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.delete("/orders/{order_id}")
def delete_order(order_id: str, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"detail": "Order deleted"} 