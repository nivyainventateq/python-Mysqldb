import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1', database='testdb')
mycursor=mydb.cursor()

# To fetch of particular data from the table

mycursor.execute("select name from employee")
result=mycursor.fetchone()
for row in result:
    print(row)

# To fetch of data from the table

mycursor.execute("select * from employee")
result=mycursor.fetchall()
for rows in result:
    print(rows)
