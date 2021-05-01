import MySQLdb

try:
    query = "insert into Student values('vedika','Computer Science','fourth Year',71)"
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="Assignment3")
    cur = mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("value inserted in table successfully.....")

except:
    if mycon != None:
        mycon.rollback()
        print("DB connection have some issue....")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")
