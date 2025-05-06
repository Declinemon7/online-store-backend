from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://postgres:password@localhost:5432/online_store')
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()