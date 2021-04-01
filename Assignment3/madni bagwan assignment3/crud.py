#creating database
import MySQLdb

try:
    query = "create database madni"
    mycon  = MySQLdb.connect(host="localhost",user="root",password="")
    cur = mycon.cursor()
    cur.execute(query)

except:
    if mycon != None:
        mycon.rollback()
        print("Error....")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")

#creating table

import MySQLdb

try:
    query = "create table info(name varchar(50),branch varchar(50),year varchar(50),rollno int(50))"
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="madni")
    cur = mycon.cursor()
    cur.execute(query)

except:
    if mycon != None:
        mycon.rollback()
        print("Error....")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")

#insert operation

import MySQLdb

try:
    query = "insert into info values('madni','CSE','BE',04)"
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="madni")
    cur = mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("data inserted in table successfully.....")

except:
    if mycon != None:
        mycon.rollback()
        print("Error....")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")

#display data

import MySQLdb

try:
    query = "select * from info"
    #we need to establish connection
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="madni")
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
        print("Error...")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")


