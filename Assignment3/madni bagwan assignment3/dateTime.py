from datetime import datetime

now = datetime.now() 


date = now.strftime("%d/%m/%Y")
print("date :",date)	

year = now.strftime("%Y")
print("year:", year)