from core import mystat_auth 
auth = mystat_auth("foros_md93", "gHrh7w*6")
token = auth.get_bearer_token()  
marks = auth.get_marks()
print(marks)
schedule = auth.get_schedule_week("2025-06-04")
print(schedule)
schedule_month = auth.get_schedule_month("2025-06-01")
print(schedule_month)
