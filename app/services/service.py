# hasattr usado para limitar erros quando o llm responde com campos inexistentes
# func usado para que a busca não seja case sensitive

from sqlalchemy.orm import Session
from app.models.autos import Autos
from sqlalchemy import func

def get_auto(params: dict, db: Session):
    query = db.query(Autos)
    data = list(params.items())

    for entry in data:
        field = entry[0]
        value = entry[1]
        if hasattr(Autos, field):
            query = query.filter(func.lower(getattr(Autos, field)) == value.lower())
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