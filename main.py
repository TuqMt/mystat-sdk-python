from core import mystat_auth 
proxies = {"http":"5435d268bba805db9446__cr.de:1ce35e8a9661e50b@gw.dataimpulse.com:10000", 
"https":"5435d268bba805db9446__cr.de:1ce35e8a9661e50b@gw.dataimpulse.com:10000"}


auth = mystat_auth("foros_md93", "gHrh7w*6", proxies=proxies)


token = auth.get_bearer_token()  
marks = auth.get_marks()
print(marks)
schedule = auth.get_schedule_week("2025-06-04")
print(schedule)
schedule_month = auth.get_schedule_month("2025-06-01")
print(schedule_month)
middle_mark = auth.middlemark()
print(middle_mark)
