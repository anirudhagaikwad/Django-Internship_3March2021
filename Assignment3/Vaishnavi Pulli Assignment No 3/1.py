from datetime import datetime

now = datetime.now() 


date_time = now.strftime("%d/%m/%Y")
print("date and time:",date_time)	

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)
© 2021 GitHub, Inc.
