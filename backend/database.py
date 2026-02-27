import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = 'sqlite:///./test.db'  # Change this to your database URL

# Create a new database engine instance
database_engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
tSession = sessionmaker(bind=database_engine)

# Create a session
def get_db_session():
    session = tSession()
    try:
        yield session
    finally:
        session.close()