from app.database.connection import Base, engine
from app.modelos.autos import Autos

if __name__ == "__main__":
    print("Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas!")
