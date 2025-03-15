import allure
import requests

from schemas.register_schema import register_success, register_unsuccess


@allure.title('Проверка успешной регистрации')
def test_register_success(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post(f'{base_url}/register', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        register_success(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 200

@allure.title('Проверка неуспешной регистрации')
def test_register_unsuccess(base_url):
    with allure.step('Отправление запроса'):
        payload = {
            "email": "sydney@fife"
        }
        response = requests.post(f'{base_url}/register', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        register_unsuccess(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 400
    with allure.step('Проверка текста ошибки'):
        assert response.json()["error"] == "Missing password"
