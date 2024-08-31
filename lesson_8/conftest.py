import pytest
import requests
from pages.employee import Employee, Company
from pages.todoMain import Task
from lesson_8.constants import X_client_URL, Todo_list_URL

@pytest.fixture
def employee_page():
    # Используйте X_client_URL для инициализации Employee
    return Employee(X_client_URL)

@pytest.fixture
def todo_page():
    # Используйте Todo_list_URL для инициализации Task
    return Task(Todo_list_URL)

@pytest.fixture
def company():
    # Создание компании
    employee_page = Employee(X_client_URL)
    company = Company(X_client_URL)
    company.create(name="Test Company")
    return company

@pytest.fixture()
def get_token(username='donatello', password='does-machines'):
    auth_data = {'username': username, 'password': password}
    response_token = requests.post(X_client_URL + '/auth/login', json=auth_data)
    token = response_token.json()['userToken']
    return token