# O uso de nullable=False visa aumentar a consistência do banco de dados, 
# porém exige uma validação de dados mais rigorosa no preenchimento dos dados.
# Esse aspecto é facilmente editável caso a fonte seja inconsistente no fornecimento de algum dado específico

# Composite indexing poderia aumentar ainda mais a performance, mas seu uso deve ser feito com cautela
# por exemplo: na indexação composta de marca e modelo faz muito sentido, 
# mas queries que não incluíssem a marca como "Quero um Corsa prata até 30 mil" podem ser prejudicadas.

# A avaliação dos dois pontos comentados deve ser feita com base na utilização real

from sqlalchemy import Column, Integer, String, Float, Boolean, Index
from app.database.connection import Base


class Autos(Base):
    __tablename__ = "autos"

    id = Column(Integer, primary_key=True)
    marca = Column(String, nullable=False, index=True)
    modelo = Column(String, nullable=False, index=True)
    ano = Column(Integer, nullable=False)
    cor = Column(String, nullable=False, index=True)
    combustivel = Column(String, nullable=False, index=True)
    kilometragem = Column(Float, nullable=False)
    preco = Column(Float, nullable=False)
    transmissao = Column(String, nullable=False, index=True)
    portas = Column(Integer, nullable=False, index=True)
    ar_condicionado = Column(Boolean, default=False, index=True)
