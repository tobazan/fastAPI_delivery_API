from dotenv import load_dotenv
import os
from sqlmodel import create_engine
from sqlmodel import Session

load_dotenv()

BD_HOST = os.getenv("BD_HOST")
BD_USER = os.getenv("BD_USER")
BD_PASSWORD = os.getenv("BD_PASSWORD")
BD_NAME = os.getenv("BD_NAME")

db_uri = f'postgresql://{BD_USER}:{BD_PASSWORD}@{BD_HOST}:5432/{BD_NAME}'
engine = create_engine(db_uri, echo=True)
session = Session(bind=engine)