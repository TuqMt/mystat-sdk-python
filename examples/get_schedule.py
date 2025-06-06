from datetime import datetime
from core import mystat_auth
client = mystat_auth('my_login', 'my_password')

today = datetime.now().strftime('%Y-%m-%d')

week_schedule = client.get_schedule_week(today)
month_schedule = client.get_schedule_month(today)

if week_schedule:
    print("Расписание на неделю:")
    for day in week_schedule:
        print(day)
else:
    print("Не удалось получить расписание на неделю.")

if month_schedule:
    print(" Расписание на месяц:")
    for day in month_schedule:
        print(day)
else:
    print("Не удалось получить расписание на месяц.")
