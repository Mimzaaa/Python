import requests
import json
from lesson_8.pages.Employee import Employee, Company

employee = Employee()
company = Company()

def test_auto(get_token):
    token = get_token
    # токен не пустой
    assert token is not None
    # токен имеет строковый формат
    assert isinstance(token, str)

def test_getcompany_id():
    company_id = company.last_active_company_id()
    # id не пустой
    assert company_id is not None
    # id только из цифр
    assert str(company_id).isdigit()

    # добавление нового сотрудника
def test_add_new_employee(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employee = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthday': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employee_id = (employee.add_new(token, body_employee))['id']
    # id сотрудника не пустой
    assert new_employee_id is not None
    # id сотрудника из цифр
    assert str(new_employee_id).isdigit()

    # получаем информацию о доб сотруднике
    info = employee.get_info(new_employee_id)
    # сравниваем  id
    assert info.json()['id'] == new_employee_id
    assert info.status_code == 200

# создание клиента без токена
def test_add_employee_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employee = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthday': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employee = employee.add_new(token, body_employee)
    assert new_employee['message'] == 'Unauthorized'

# создание клиента без тела запроса
def test_add_employee_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employee = {}
    new_employee = employee.add_new(token, body_employee)
    assert new_employee['message'] == 'Internal server error'

def test_get_employee():
    com_id = company.last_active_company_id()
    list_employee = employee.get_list(com_id)
    assert isinstance(list_employee, list)

# обязательное поле id компании в запросе на получение списка работников - без id компании
def test_get_list_employee_missing_company_id():
    try:
        employee.get_list()
    except TypeError as e:
        assert str(e) == "Employee.get_list() missing 1 required positional argument: 'company_id'"