# hasattr usado para limitar erros quando o llm responde com campos inexistentes
# func usado para que a busca não seja case sensitive

from sqlalchemy.orm import Session
from app.models.autos import Autos
from sqlalchemy import func

def get_auto(params: dict, db: Session):
    print(f"[DEBUG] Parâmetros recebidos: {params}")
    query = db.query(Autos)
    data = list(params.items())
    for entry in data:
        field = entry[0]
        value = entry[1]
        if hasattr(Autos, field):
            if isinstance(value, str):
                query = query.filter(func.lower(getattr(Autos, field)) == value.lower())
            else: # Para caso de não-strings que não podem ter lower
                query = query.filter(getattr(Autos, field) == value)
        elif field == "max_price":
            query = query.filter(Autos.preco <= value)
        elif field == "max_km":
            query = query.filter(Autos.kilometragem <= value)
        elif field == "ano_min":
            query = query.filter(Autos.ano >= value)
    results = query.all()

    res = []
    for auto in results:
        res.append({
            "marca": auto.marca,
        "modelo": auto.modelo,
        "ano": auto.ano,
        "cor": auto.cor,
        "kilometragem": auto.kilometragem,
        "preco": auto.preco,
        "transmissao": auto.transmissao,
        "combustivel": auto.combustivel,
        "portas": auto.portas,
        "ar_condicionado": "Sim" if auto.ar_condicionado else "Não"
        })
    return res