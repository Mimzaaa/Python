import requests
from constants import Todo_list_URL

class Task:
    BASE_URL = f"{Todo_list_URL}/tasks"

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.get_token()}"}

    def get_token(self):
        # Функция для получения токена
        # Реализуйте здесь логику авторизации
        return "dummy_token"

    def get_list(self):
        response = requests.get(self.BASE_URL, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create(self, data):
        response = requests.post(self.BASE_URL, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def rename(self, task_id, new_name):
        response = requests.patch(f"{self.BASE_URL}/{task_id}", json={"name": new_name}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def info(self, task_id):
        response = requests.get(f"{self.BASE_URL}/{task_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def change_status(self, task_id, status):
        response = requests.patch(f"{self.BASE_URL}/{task_id}", json={"completed": status}, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete(self, task_id):
        response = requests.delete(f"{self.BASE_URL}/{task_id}", headers=self.headers)
        response.raise_for_status()
        return response.status_code
