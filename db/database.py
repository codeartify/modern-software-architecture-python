from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using an in-memory SQLite DB for demonstration.
DATABASE_URL = "sqlite:///./test.db"  # This creates a persistent file

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
