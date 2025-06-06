import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core import mystat_auth  

def test_case_1():
    auth = mystat_auth("foros_md93", "gHrh7w*6", proxies={})
    return auth.get_auth()[0] == True 
def test_case_2():
    auth = mystat_auth("Ivas_keko83", "bg&u3uh8")
    return auth.get_auth()[0] == False
def test_case_3():
    auth = mystat_auth("Grr_dervr70", "YGbueg7dg")
    return auth.get_auth()[0] == False
print("Тест 1:", "Пройден" if test_case_1() else "Не пройден")
print("Тест 2:", "Пройден" if test_case_2() else "Не пройден")
print("Тест 3:", "Пройден" if test_case_3() else "Не пройден")