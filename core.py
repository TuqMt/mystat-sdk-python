import time
import requests
import config

class mystat_auth:
    TOKEN_LIFETIME = 7200  

    def __init__(self, login, password):
        self.login = login
        self.password = password



    def get_auth(self):
        url = 'https://mapi.itstep.org/v1/mystat/auth/login'
        response = requests.post(url, json={
            'login': self.login,
            'password': self.password
        })

        if response.status_code == 200:
            config.timecode = time.time()
            config.Bearer = response.text.strip('"')  
            print("[INFO] Новый токен успешно получен.")
            return config.Bearer
        else:
            print(f"[ERROR] Ошибка авторизации: {response.status_code} — {response.text}")
            return None



    def is_token_valid(self):
        if hasattr(config, 'timecode') and hasattr(config, 'Bearer') and config.Bearer:
            elapsed = time.time() - config.timecode
            return elapsed < mystat_auth.TOKEN_LIFETIME
        return False



    def get_bearer_token(self):
        if not self.is_token_valid():
            return self.get_auth()
        print("[INFO] Используется сохранённый токен.")
        return config.Bearer




    def get_marks(self):
        if not self.is_token_valid():
            print("[ERROR] Токен недействителен, требуется повторная авторизация.")
            return None

        url = 'https://mapi.itstep.org/v1/mystat/aqtobe/statistic/marks'
        headers = {
            'Authorization': f'Bearer {config.Bearer}'
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
        url=f"https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-month?type=week&date_filter={date}"
        headers = {
            'Authorization': f'Bearer {config.Bearer}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"[ERROR] Ошибка получения расписания: {response.status_code} — {response.text}")
            return None
        


    def get_schedule_month(self, date):
        if not self.is_token_valid():
            print("[ERROR] Токен недействителен, требуется повторная авторизация.")
            return None
        url=f'https://mapi.itstep.org/v1/mystat/aqtobe/schedule/get-existing-schedule?date_filter={date}'
        headers = {
            'Authorization': f'Bearer {config.Bearer}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
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
