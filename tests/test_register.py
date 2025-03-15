import requests
from jsonschema import validate

url = 'https://reqres.in/api/users'

payload = {
    "name": "morpheus",
    "job": "leader"
}

def test():
    response = requests.post(url, data=payload, verify=False)
    body = response.json()
    assert response.status_code == 201
    validate(body, schema=)