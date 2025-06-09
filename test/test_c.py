import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import mystat_auth

# Заменить на актуальные данные для тестов
VALID_LOGIN = "foros_md93"
VALID_PASSWORD = "gHrh7w*6"

# Тест 1: Успешная авторизация
def test_case_1():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    return auth.get_auth()[0] == True

# Тест 2: Неверный логин/пароль
def test_case_2():
    auth = mystat_auth("Grr_dervr70", "YGbueg7dg")
    return auth.get_auth()[0] == False

def test_case_3():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    auth.get_auth()
    return auth.is_token_valid() == True

def test_case_4():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    token1 = auth.get_bearer_token()
    token2 = auth.get_bearer_token()
    return (token1 == token2) == True

def test_case_5():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    auth.get_auth()
    marks = auth.get_marks()
    return (type(marks) == list or marks is None) == True

def test_case_6():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    auth.get_auth()
    result = auth.middlemark()
    return (type(result) == float or type(result) == int or result is None) == True

def test_case_7():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    auth.get_auth()
    result = auth.get_schedule_week("2025-06-09")
    return (type(result) == dict or result is None) == True

def test_case_8():
    auth = mystat_auth(VALID_LOGIN, VALID_PASSWORD)
    auth.get_auth()
    result = auth.get_schedule_month("2025-06-01")
    return (type(result) == dict or result is None) == True

print("Тест 1 (Успешная авторизация):", test_case_1())
print("Тест 2 (Неверный логин/пароль):", test_case_2())
print("Тест 3 (Проверка валидности токена):", test_case_3())
print("Тест 4 (Повторное получение токена):", test_case_4())
print("Тест 5 (Получение оценок):", test_case_5())
print("Тест 6 (Средняя оценка):", test_case_6())
print("Тест 7 (Получение расписания на неделю):", test_case_7())
print("Тест 8 (Получение расписания на месяц):", test_case_8())





