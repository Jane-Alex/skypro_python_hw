import pytest
import requests

base_url = "https://x-clients-be.onrender.com"


@pytest.fixture()
def get_token(user = 'bloom', password = 'fire-fairy'):
    creds = {
        'username': user,
        'password': password
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    return resp.json()["userToken"]
