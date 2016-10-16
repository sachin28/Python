import pymysql

password = raw_input("input password of the db: ")

try:
    db = pymysql.connect("localhost","root",password,"test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()

    print ("Database version : %s " % data)
    db.close()

except:
    print "Wrong Password"



