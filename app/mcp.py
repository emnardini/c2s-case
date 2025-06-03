# hasattr usado para limitar erros quando o llm responde com campos inexistentes

from sqlalchemy.orm import Session
from app.modelos.autos import Autos

def get_auto(params: dict, db: Session):
    query = db.query(Autos)
    data = list(params.items())

    for entry in data:
        field = entry[0]
        value = entry[1]
        if hasattr(Autos, field):
            query = query.filter(getattr(Autos, field) == value)
    results = query.all()

    res = []
    for auto in results:
        res.append({
            "marca": auto.marca,
            "modelo": auto.modelo,
            "ano": auto.ano,
            "cor": auto.cor,
            "kilometragem": auto.kilometragem,
            "preco": auto.preco
        })
    return res