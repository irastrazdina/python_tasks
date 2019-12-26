import datetime
 
date_a = datetime.datetime(2018, 11, 20, 21, 20, 31)
print(date_a)
date_now = datetime.datetime.now()
delta = date_now - date_a
hours = delta.total_seconds() // 3600
minutes = hours * 60
 
print("Days gone: ", delta.days)
print("Hours gone: ", hours)
print("Minutes gone: ", minutes)
print("Seconds gone: ", delta.total_seconds())
