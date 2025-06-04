import time
import requests


class mystat_auth:
    TOKEN_LIFETIME = 7200

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.Bearer = ''
        self.timecode = 0

    def get_auth(self):
        url = 'https://mapi.itstep.org/v1/mystat/auth/login'
        response = requests.post(url, json={
            'login': self.login,
            'password': self.password
        })

        if response.status_code == 200:
            self.timecode = time.time()
            self.Bearer = response.text.strip('"')  
            print("[INFO] Новый токен успешно получен.")
            return self.Bearer
        else:
            print(f"[ERROR] Ошибка авторизации: {response.status_code} — {response.text}")
            return None

    def is_token_valid(self):
        elapsed = time.time() - self.timecode
        return self.Bearer and elapsed < self.TOKEN_LIFETIME

    def get_bearer_token(self):
        if not self.is_token_valid():
            return self.get_auth()
        print("[INFO] Используется сохранённый токен.")
        return self.Bearer

    def get_marks(self):
        if not self.is_token_valid():
            print("[ERROR] Токен недействителен, требуется повторная авторизация.")
            return None

        url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'
        headers = {
            'Authorization': f'Bearer {self.Bearer}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            marks = [int(item['mark']) for item in data if 'mark' in item]
            return marks
        else:
            print(f"[ERROR] Ошибка получения оценок: {response.status_code} — {response.text}")
            return None

    def get_schedule_week(self, date):
        if not self.is_token_valid():
            print("[ERROR] Токен недействителен, требуется повторная авторизация.")
            return None
        url = f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week&date_filter={date}"
        headers = {
            'Authorization': f'Bearer {self.Bearer}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Ошибка получения расписания: {response.status_code} — {response.text}")
            return None

    def get_schedule_month(self, date):
        if not self.is_token_valid():
            print("[ERROR] Токен недействителен, требуется повторная авторизация.")
            return None
        url = f'https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-existing-schedule?date_filter={date}'
        headers = {
            'Authorization': f'Bearer {self.Bearer}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Ошибка получения расписания: {response.status_code} — {response.text}")
            return None

    def middlemark(self):
        marks = self.get_marks()
        if marks is None:
            return None
        if not marks:
            return 0
        return sum(marks) / len(marks)
