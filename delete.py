import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1', database='testdb')
mycursor=mydb.cursor()

# delete a row from an existing table

# data="delete from employee where name='raj'"
# mycursor.execute(data)
# mydb.commit()


# fetch the data after updating deleting

mycursor.execute("select * from employee")
result=mycursor.fetchall()
for row in result:
    print(row)

print(mycursor.rowcount, "record(s) deleted")