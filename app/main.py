from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.mcp import get_auto

app = FastAPI()

def db_lifecycle():
    print("Criando sessão com o banco")
    db = SessionLocal()
    try:
        yield db
        print("Requisição finalizada")
    finally:
        print("Fechando sessão")
        db.close()

@app.post("/mcp/search")
def search(params: dict, db: Session = Depends(db_lifecycle)):
    results = get_auto(params, db)
    return results
