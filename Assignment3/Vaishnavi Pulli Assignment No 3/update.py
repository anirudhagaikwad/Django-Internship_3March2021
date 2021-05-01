import MySQLdb

try:
    query = "update Student set rollno='39' where name='vaish'"
    #we need to establish connection
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="Assignment3")
    #to perform any operation we need to   create cursor object
    cur = mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("values are update...")
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
