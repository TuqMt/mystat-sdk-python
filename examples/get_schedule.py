from datetime import datetime
from core import mystat_auth

# Создаём клиента с авторизацией
client = mystat_auth('my_login', 'my_password')

# Получаем текущую дату в формате YYYY-MM-DD
today = datetime.now().strftime('%Y-%m-%d')

# Получаем расписание на неделю, начиная с сегодняшнего дня
week_schedule = client.get_schedule_week(today)

# Получаем расписание на месяц, начиная с сегодняшнего дня
month_schedule = client.get_schedule_month(today)

# Выводим недельное расписание, если оно есть
if week_schedule:
    print("📅 Расписание на неделю:")
    for day in week_schedule:
        print(day)
else:
    print("Не удалось получить расписание на неделю.")

# Выводим месячное расписание, если оно есть
if month_schedule:
    print("📆 Расписание на месяц:")
    for day in month_schedule:
        print(day)
else:
    print("Не удалось получить расписание на месяц.")

