# Se por alguma razão para nossa utilização for melhor que o banco seja atualizado após cada query,
# atualizar o valor do autoflush para true. 

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=path)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
