import pytest


def pytest_collection_modifyitems(items):
    order = ['test_register.py', 'test_login.py', 'test_user.py']
    items.sort(key=lambda x: order.index(x.nodeid.split("::")[0]))

@pytest.fixture
def base_url():
    base_url = 'https://reqres.in/api'

    return base_url
