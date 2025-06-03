# Para implementações futuras, com mais tempo eu faria as seguintes modificações:
# 1. gerar os arquivos json de parâmetros dinamicamente, para garantir que a lista de marcas seja sempre atualizada automaticamente;
# 2. implementação de uma lib de fuzzy search, para lidar com typos
# 3. gerar um dicionário de normalização com grafias comuns de algumas marcas, como vw > volkswagen e alfa > alfa romeo
# 4. tratar melhor casos onde quilometragem e preço são usados juntos no prompt
# 5. tratar melhor casos onde o usuário pode pedir mais de um termo: ex: "quero um carro preto ou vermelho"
# Infelizmente fiquei sem tempo para essas implementações

import json
import os
import re
import requests

BASE_URL = "http://localhost:8000/mcp/search"

def load_params(filename):
    try:
        path = os.path.join("parameters", filename)
        file = open(path, "r", encoding="utf-8")
        content = json.load(file)
        file.close()
        return content
    except Exception as exc:
        print(f"Erro inesperado ao carregar {filename}: {exc}")
        return []

MAP = {
    "marca": load_params("marcas.json"),
    "cor": load_params("cores.json"),
    "combustivel": load_params("combustiveis.json"),
    "transmissao": load_params("transmissoes.json"),
    "modelo": load_params("modelos.json"),
    "portas": load_params("portas.json"),
    "ar_condicionado": load_params("ar_condicionado.json"),
}

def max_price(prompt):
    if "km" in prompt or "quilometros" in prompt or "quilômetros":
        return None
    num = re.findall(r"\d+", prompt)
    if not num:
        return None
    price = num[0].replace(".", "")
    return int(price) * 1000 if "mil" in prompt else int(price)

def max_km(prompt):
    if "r$" in prompt or "reais" in prompt or "mil reais" in prompt:
        return None
    if "km" not in prompt and "quilometro" not in prompt and "quilômetro" not in prompt:
        return None
    num = re.findall(r"\d+", prompt)
    if not num:
        return None
    km = num[0].replace(".", "")
    return int(km) * 1000 if "mil" in prompt else int(km)

def user_prompt():
    filters = {}
    prompt = input("Que carro você está procurando?\n> ")
    prompt = prompt.lower()
    for field in MAP:
        possible_terms = MAP[field]
        for term in possible_terms:
            lowercase_term = str(term).lower()
            if lowercase_term in prompt:
                filters[field] = term
                break
    price = max_price(prompt)
    if price:
        filters["max_price"] = price
    km = max_km(prompt)
    if km:
        filters["max_km"] = km
    return filters


def send_to_server(filters):
    try:
        response = requests.post(BASE_URL, json=filters)
        response.raise_for_status()
        return response.json()
    except Exception as error:
        print(f"Erro ao consultar o servidor: {error}")
        return []

def show_results(results):
    if not results:
        print("Nenhum carro encontrado.")
        return
    print(f"{len(results)} carros encontrados:\n")
    for item in results:
        print(f"- {item['marca']} {item['modelo']} | {item['ano']} | {item['cor']} | {item['kilometragem']} km | R$ {item['preco']:.2f}")

def main():
    print("Iniciando busca de veículos...")
    filters = user_prompt()
    results = send_to_server(filters)
    show_results(results)
# Evita rodar automaticamente em caso de chamada por outro arquivo
if __name__ == "__main__":
    main()