# mystat_auth

Класс для авторизации и получения данных из API MyStat — личного кабинета ITStep.
https://mystat.itstep.org/
# Позволяет:

Авторизоваться и получить токен доступа (Bearer Token)

Получать оценки студента

Получать расписание на неделю и на месяц

Вычислять средний балл

# Установка
Для работы требуется Python 3 и библиотека requests.

Установите requests, если ещё не установлена:
    pip install requests


# Использование
from mystat_auth import MyStatAuth  # если класс сохранён в файле mystat_auth.py

# Создание объекта с логином и паролем
client = MyStatAuth(login='your_login', password='your_password')

# Получение токена (автоматически вызывается при необходимости)
token = client.get_bearer_token()
print("Токен:", token)

# Получить оценки
marks = client.get_marks()
print("Оценки:", marks)

# Вычислить средний балл
average = client.middlemark()
print("Средний балл:", average)

# Получить расписание на неделю (пример с датой в формате 'YYYY-MM-DD')
schedule_week = client.get_schedule_week('2023-06-01')
print("Расписание на неделю:", schedule_week)

# Получить расписание на месяц (пример с датой в формате 'YYYY-MM-DD')
schedule_month = client.get_schedule_month('2023-06-01')
print("Расписание на месяц:", schedule_month)

# Создание объекта с логином и паролем
client = MyStatAuth(login='your_login', password='your_password')

# Получение токена (автоматически вызывается при необходимости)
token = client.get_bearer_token()
print("Токен:", token)

# Получить оценки
marks = client.get_marks()
print("Оценки:", marks)

# Вычислить средний балл
average = client.middlemark()
print("Средний балл:", average)

# Получить расписание на неделю (пример с датой в формате 'YYYY-MM-DD')
schedule_week = client.get_schedule_week('2023-06-01')
print("Расписание на неделю:", schedule_week)

# Получить расписание на месяц (пример с датой в формате 'YYYY-MM-DD')
schedule_month = client.get_schedule_month('2023-06-01')
print("Расписание на месяц:", schedule_month)


# Параметры конструктора
login — логин пользователя (строка)

password — пароль пользователя (строка)

proxies — словарь с прокси для запросов (опционально)

pause — пауза между запросами в секундах (по умолчанию 0.5)

# Методы
get_bearer_token() — возвращает текущий или новый токен авторизации

get_marks() — возвращает список оценок (числа), либо None при ошибке

middlemark() — возвращает среднее значение оценок, либо None, если оценок нет

get_schedule_week(date) — возвращает JSON с расписанием на неделю по дате

get_schedule_month(date) — возвращает JSON с расписанием на месяц по дате

Особенности
Токен живёт 2 часа (7200 секунд). При истечении срока автоматически обновляется.

Все запросы делают небольшую паузу (0.5 с) для снижения нагрузки на сервер.

Обработка ошибок и вывод сообщений происходит через logging (можно настроить уровень логирования).
