from app.services.service import get_auto
from app.database.connection import SessionLocal

def test_filter_by_brand(): # Verifica filtro de marca
    db = SessionLocal()
    params = {"marca": "Fiat"}
    results = get_auto(params, db)
    assert all(auto["marca"] == "Fiat" for auto in results)

def test_filter_by_year(): # Verifica filtro de ano
    db = SessionLocal()
    params = {"ano": 2020}
    results = get_auto(params, db)
    assert all(auto["ano"] == 2020 for auto in results)

def test_invalid_filter(): # Testa marca inexistente
    db = SessionLocal()
    params = {"marca": "Xablaberry"}
    results = get_auto(params, db)
    assert results == []
