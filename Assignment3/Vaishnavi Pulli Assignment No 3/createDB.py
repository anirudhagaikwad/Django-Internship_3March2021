import MySQLdb

try:
    query = "create database Assignment3"
    mycon  = MySQLdb.connect(host="localhost",user="root",password="")
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
