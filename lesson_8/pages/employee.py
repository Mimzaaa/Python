import requests
from lesson_8.constants import X_client_URL

path = '/employee/'

class Employee:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_list(self):
        response = requests.get(self.base_url + '/employee', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def add_new(self, data):
        response = requests.post(self.base_url + '/employee', json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_info(self, emp_id):
        response = requests.get(self.base_url  + path, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def change_info(self, emp_id, data):
        response = requests.patch(self.base_url  + path, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

class Company:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create(self, name):
        response = requests.post(self.base_url + '/company', json={"name": name}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def last_active_company_id(self):
        response = requests.get(self.base_url + '/company/last', headers=self.headers)
        response.raise_for_status()
        return response.json()["id"]
