from typing import Any
from lesson_8.pages.employee import Company, Employee
import requests

def test_auto(get_token: Any):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

def test_get_list(employee_page: Employee):
    employees = employee_page.get_list()
    assert isinstance(employees, list)

# добавление нового сотрудника
def test_add_new_employee(employee_page: Employee, get_token: Any):
    token = str(get_token)
    new_employee = {"name": "John Doe", "position": "Developer", "salary": 50000}
    employee = employee_page.add_new(new_employee)
    assert employee["name"] == new_employee["name"]

def test_get_employee_info(employee_page: Employee, company: Company):
    # Создаем сотрудника и получаем его информацию
    new_employee = {"name": "Jane Doe", "position": "Tester", "salary": 45000}
    employee = employee_page.add_new(new_employee)
    emp_id = employee["id"]
    info = employee_page.get_info(emp_id)
    assert info["id"] == emp_id

def test_change_employee_info(employee_page: Employee):
    new_employee = {"name": "Mark Smith", "position": "Manager", "salary": 60000}
    employee = employee_page.add_new(new_employee)
    emp_id = employee["id"]
    updated_data = {"name": "Mark Smith Updated", "position": "Senior Manager", "salary": 65000}
    updated_employee = employee_page.change_info(emp_id, updated_data)
    assert updated_employee["name"] == updated_data["name"]
