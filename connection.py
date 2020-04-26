import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Nivya@mysql1')
print(mydb)

# Checking the Database Connection

if(mydb):
    print("connecction sucessful")
else:
    print("connection unsucessful")