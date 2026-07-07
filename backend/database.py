from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker



Base = declarative_base()
engine = create_engine("sqlite:///fim.db")
Session = sessionmaker(bind=engine)

class FileRecord(Base):
    __tablename__ = "files"

    path = Column(String, primary_key=True)
    hash = Column(String)

Base.metadata.create_all(engine)    