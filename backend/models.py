from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "sqlite:///./orders.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True, index=True)
    status = Column(String)
    order_time = Column(String)
    purchase_time = Column(String, nullable=True)
    ship_time = Column(String, nullable=True)
    arrival_time = Column(String, nullable=True)
    amazon_estimated_arrival_time = Column(String, nullable=True)

Base.metadata.create_all(bind=engine) 