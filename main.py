import uvicorn
from fastapi import FastAPI
from db.database import Base, engine, SessionLocal
from controller.reserve_tickets_controller import router as reserve_tickets_router

app = FastAPI()

# Create tables if needed (assuming SQLAlchemy models)
Base.metadata.create_all(bind=engine)

app.include_router(reserve_tickets_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
