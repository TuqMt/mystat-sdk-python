from core import mystat_auth
client = mystat_auth('my_login', 'my_password')

average = client.middlemark()

if average is not None:
    print(f"Средний балл: {average:.2f}")
else:
    print("Ошибка при вычислении среднего балла.")
