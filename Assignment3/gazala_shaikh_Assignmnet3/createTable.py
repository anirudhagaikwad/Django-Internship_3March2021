import MySQLdb

try:
    query = "create table Studentinfo(name varchar(50),branch varchar(50),year varchar(50),rollno int(50))"
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="Assignment3")
    cur = mycon.cursor()
    cur.execute(query)

except:
    if mycon != None:
        mycon.rollback()
        print("DB connection have some issue....")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")