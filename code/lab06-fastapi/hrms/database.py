from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database URL, the database will be stored in the current directory
DATABASE_URL = "sqlite:///./hrm.db"

# Create an engine to interact with the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
