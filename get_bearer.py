from core import mystat_auth
# Настройка прокси (если требуется, например, для обхода ограничений)
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

# Создаём экземпляр класса, передаём логин, пароль и прокси
client = mystat_auth('my_login', 'my_password', proxies=proxies)

# Получаем токен. Если токен устарел — автоматически обновится
token = client.get_bearer_token()

# Получаем список оценок
marks = client.get_marks()

# Выводим оценки, если удалось получить
if marks is not None:
    print("Оценки:", marks)
else:
    print("Не удалось получить оценки.")
