import allure
import requests
from schemas.login_schema import login_success, login_unsuccess


@allure.title('Проверка успешного входа')
def test_success_login(base_url):
    with allure.step('Отправка запроса'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(f'{base_url}/login', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        login_success(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 200

@allure.step('Проверка неуспешного входа')
def test_unsuccess_login(base_url):
    with allure.step('Отправка запроса'):
        payload = {
            "email": "peter@klaven"
        }
        response = requests.post(f'{base_url}/login', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        login_unsuccess(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 400
    with allure.step('Проверка текста ошибки'):
        assert response.json()["error"] == "Missing password"