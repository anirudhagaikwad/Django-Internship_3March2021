from datetime import datetime

now = datetime.now() # current date and time


date_time = now.strftime("%d/%m/%Y")
print("date and time:",date_time)	

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)
