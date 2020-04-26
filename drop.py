import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root", password='Nivya@mysql1',database='testdb')
x=mydb.cursor()

x.execute("drop table customer")
mydb.commit()
print("Table sucessfully deleted")
