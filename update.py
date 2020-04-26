import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1', database='testdb')
mycursor=mydb.cursor()


# updating a value to a existing table

modify=" UPDATE customer SET  address='kerela' where name='dolly' "
mycursor.execute(modify)
mydb.commit()

# fetch the data after updating

mycursor.execute("select * from customer")
result=mycursor.fetchall()
for row in result:
    print(row)

print(mycursor.rowcount, "record(s) affected")