import MySQLdb

try:
    query = "select * from Student"
    #we need to establish connection
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="Assignment3")
    #to perform any operation we need to   create cursor object
    cur = mycon.cursor()
    cur.execute(query)
    tdata = cur.fetchall()
    print("value fetch successfully.........")
    for row in tdata:
        print("\n name : ",row[0])
        print("\n stdage : ",row[1])
        print("\n address : ",row[2])

except:
    if mycon != None:
        mycon.rollback()
        print("DB connection have some issue.... value not fetch......")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")
© 2021 GitHub, Inc.
