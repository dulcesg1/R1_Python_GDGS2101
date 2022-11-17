import json
from urllib import response
from app import app
INFO = {
    "pastasdos": {
        "pr":"Penne Rigate",
        "ft":"Fusilli Tricolor",
        "sa":"Spaghettini de Arroz",
    },
    "pastasuno":{
        "r":"Ramen",
        "m":"Macarrones",
        "f":"Farfalle",
    },
    "noodles":{
        "UD":"UDON",
        "SO":"SOBA",
        "SOM":"SOMEN",
    }
}
INFOW = {
    "pastasdo": {
        "pr":"Penne Rigate",
        "ft":"Fusilli Tricolor",
        "sa":"Spaghettini de Arroz",
    },
    "pastasuno":{
        "r":"Ramen",
        "m":"Macarrones",
        "f":"Farfalle",
    },
    "noodles":{
        "UD":"UDON",
        "SO":"SOBA",
        "SOM":"SOMEN",
    }
}
def test_all_pastas():
    response = app.test_client().get('http://192.168.0.7:3200/json')
    res = json.loads(response.data.decode('utf-8')).get("Pastas")
    assert response.status_code == 200
    assert res== INFOW
def test_all_pastasw():
    response = app.test_client().get('http://192.168.0.7:3200/json')
    res = json.loads(response.data.decode('utf-8')).get("Pastas")
    assert response.status_code == 200
    assert res== INFOW    

def test_SOM_pasta():
    response = app.test_client().get('http://192.168.0.7:3200/json/noodles/SOM')
    res = json.loads(response.data.decode('utf-8')).get("res")
    assert response.status_code == 200
    assert res== INFOW["noodles"]["SOM"]


