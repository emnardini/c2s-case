from app.database.connection import SessionLocal
from app.models.autos import Autos

session = SessionLocal()

veiculos = session.query(Autos).all()
print(f"{len(veiculos)} veículos encontrados:\n")
for v in veiculos:
    print(f"{v.id} - {v.marca} {v.modelo}, {v.ano}, {v.cor}, R${v.preco:.2f} | "
          f"{v.kilometragem:.1f} km | {v.transmissao} | {v.portas} portas | "
          f"{'Ar Cond.' if v.ar_condicionado else 'Sem Ar'}")
session.close()
