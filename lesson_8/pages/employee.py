import requests
import json
from lesson_8.constants import X_client_URL

path = '/employee/'

class Company:

    def __init__(self, url=X_client_URL):
        self.url = url
    
    # создание компании
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/company', headers=headers, params=body)
        return response.json()

    # последняя созданная активная компания
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        response = requests.get(self.url + '/company', params=active_params)
        return response.json()[-1]["id"]

class Employee:

    def __init__(self, url=X_client_URL):
        self.url = url

    # список сотрудников компании
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    # добавление сотрудника в компании
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/employee', headers=headers, json=body)
        return response.json()

    # получение информации о сотруднике
    def get_info(self, employee_id: int):
        response = requests.get(self.url  + path + str(employee_id))
        return response

    # изменеие информации о сотруднике
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url  + path + str(employee_id), headers=headers)
        return response