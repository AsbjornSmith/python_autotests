import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='da90db636fdeb79b9098bc8f40f207ab'
HEADER={'Content-Type':'application/json'}
TRAINER_ID=21353
TRAINER_NAME='Valdr'
TRAINER_CITY='Paradise'

def test_status_code():
    response_status_code=requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response_status_code.status_code==200

def test_trainer_name():
    response_trainer_name=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID}, headers=HEADER)
    assert response_trainer_name.json()['data'][0]['trainer_name']==TRAINER_NAME

@pytest.mark.parametrize('key, value', [('trainer_name', TRAINER_NAME), ('level', '1'), ('is_premium', True), ('city', TRAINER_CITY)])

def test_parametrize(key, value):
    response_parametrize=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID}, headers=HEADER)
    assert  response_parametrize.json()['data'][0][key]==value