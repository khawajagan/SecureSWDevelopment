from sqlalchemy import create_engine
from models import Base

# SQLite database URL
DATABASE_URL = "sqlite:///./hrm.db"

# Create an engine to interact with the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all the tables in the database
Base.metadata.create_all(bind=engine)
