from app.database.connection import engine
import traceback

try:
    with engine.connect() as connection:
        print("Conexão com o banco de dados OK!")
except Exception as e:
    print("Erro ao conectar: trace:")
    traceback.print_exc()
