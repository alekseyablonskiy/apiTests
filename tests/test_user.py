import allure
import requests
from schemas.user_schema import create_user, update_user, get_user


@allure.step('Проверка создания пользователя')
def test_create_user(base_url):
    with allure.step('Отправка запроса'):
        payload = {
        "name": "morpheus",
        "job": "leader"
        }
        response = requests.post(f'{base_url}/users', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        create_user(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 201

@allure.step('Проверка обновления пользователя')
def test_update_user(base_url):
    with allure.step('Отправка запроса'):
        payload = {
        "name": "morpheus",
        "job": "zion resident"
        }
        response = requests.put(f'{base_url}/users/2', data=payload, verify=False)
    with allure.step('Проверка схемы'):
        update_user(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 200

@allure.step('Проверка информации пользователя')
def test_get_user(base_url):
    with allure.step('Отправка запроса'):
        response = requests.get(f'{base_url}/users/2', verify=False)
    with allure.step('Проверка схемы'):
        get_user(response.json())
    with allure.step('Проверка кода'):
        assert response.status_code == 200

@allure.step('Проверка удаления пользователя')
def test_delete_user(base_url):
    with allure.step('Отправка запроса'):
        response = requests.delete(f'{base_url}/users/2', verify=False)
    with allure.step('Проверка кода'):
        assert response.status_code == 204
    with allure.step('Проверка ответа'):
        assert response.text == ''

@allure.step('Поиск несуществующего пользователя')
def test_user_not_found(base_url):
    with allure.step('Отправка запроса'):
        response = requests.get(f'{base_url}/users/23', verify=False)
    with allure.step('Проверка кода'):
        assert response.status_code == 404