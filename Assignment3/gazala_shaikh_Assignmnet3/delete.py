import MySQLdb

try:
    query = "delete from studentinfo where branch='Mechanical'"
    #we need to establish connection
    mycon = MySQLdb.connect(host="localhost",user="root",password="",database="Assignment3")
    #to perform any operation we need to   create cursor object
    cur = mycon.cursor()
    cur.execute(query)
    mycon.commit()
    print("\n record deleted successfully...")
    

except:
    print("record is not deleted......")

finally:
    cur.close()
    print("cursor close")
    mycon.close()
    print("connection close")