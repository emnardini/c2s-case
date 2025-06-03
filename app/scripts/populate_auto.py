import random
from app.models.autos import Autos
from app.database.connection import SessionLocal
import sys

session = SessionLocal()

marca_modelo = {
    "Fiat": ["Uno", "Palio", "Argo", "Toro", "Cronos", "Mobi"],
    "Ford": ["Fiesta", "Ka", "Ecosport", "Fusion", "Mustang"],
    "Volkswagen": ["Gol", "Voyage", "Polo", "T-Cross", "Virtus"],
    "Chevrolet": ["Onix", "Prisma", "Celta", "Cruze"],
    "Toyota": ["Corolla", "Etios", "Hilux", "Yaris"],
    "Honda": ["Civic", "Fit", "City"]
}
cores = ["Preto", "Branco", "Prata", "Vermelho", "Azul", "Chumbo"]
combustiveis = ["Gasolina", "Álcool", "TotalFlex", "Diesel"]
transmissoes = ["Manual", "Automática"]
n_portas = [2, 4]

def gerar_carro():
    marca = random.choice(list(marca_modelo.keys()))
    modelo = random.choice(marca_modelo[marca])
    ano = random.randint(2000, 2023)
    cor = random.choice(cores)
    combustivel = random.choice(combustiveis)
    kilometragem = round(random.uniform(7000, 190000), 1)
    transmissao = random.choice(transmissoes)
    portas = random.choice(n_portas)
    ar_condicionado = random.choice([True, False])
    if marca in ["Toyota", "Honda"]:
        preco = round(random.uniform(70000, 190000), 2)
    else:
        preco = round(random.uniform(18000, 110000), 2)

    return Autos(
        marca=marca,
        modelo=modelo,
        ano=ano,
        cor=cor,
        combustivel=combustivel,
        kilometragem=kilometragem,
        preco=preco,
        transmissao=transmissao,
        portas=portas,
        ar_condicionado=ar_condicionado
    )

for i in range(142):
    carro = gerar_carro()
    session.add(carro)
session.commit() # Caso optemos por autocommit=true no SessionLocal comentar essa linha
session.close()
print("Veículos gerados.")