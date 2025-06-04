from core import mystat_auth 
auth = mystat_auth("foros_md93", "gHrh7w*6")
token = auth.get_bearer_token()  
marks = auth.get_marks()
print(marks)
