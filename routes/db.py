# routes/db.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

ENGINE = create_engine("sqlite:///nutrition.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=ENGINE)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    age = Column(Integer)
    gender = Column(String)
    height_cm = Column(Float)
    weight_kg = Column(Float)
    activity_level = Column(String)
    goal = Column(String)
    diet_type = Column(String)
    extras = Column(JSON)

class FoodLog(Base):
    __tablename__ = "food_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    date = Column(Date, default=datetime.date.today)
    items = Column(JSON)  # list of items with nutrition
    total_calories = Column(Float, default=0.0)

def init_db():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    init_db()
