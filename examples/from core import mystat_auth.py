from core import mystat_auth
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

client = mystat_auth('my_login', 'my_password', proxies=proxies)

token = client.get_bearer_token()  # Получаем Bearer-токен (автоматически обновляется)
marks = client.get_marks()

if marks is not None:
    print("Оценки:", marks)
else:
    print("Не удалось получить оценки.")
