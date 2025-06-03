from client.agent import parse_user_request

def test_simple_request(): # Testa request simples
    user_input = "Quero um Volkswagen azul"
    filters = parse_user_request(user_input)
    expected = {"marca": "Volkswagen", "cor": "Azul"}
    assert filters == expected

def test_request_with_price_range(): # Testa preço máximo
    user_input = "Procuro um carro preto até 40 mil"
    filters = parse_user_request(user_input)
    assert filters["cor"] == "Preto"
    assert filters["max_price"] == 40000
