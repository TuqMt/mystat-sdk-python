from core import mystat_auth
# Создаём экземпляр без прокси
client = mystat_auth('my_login', 'my_password')

# Вызываем метод для подсчёта среднего балла
average = client.middlemark()

# Если средний балл посчитан успешно — выводим его
if average is not None:
    print(f"Средний балл: {average:.2f}")
else:
    print("Ошибка при вычислении среднего балла.")

