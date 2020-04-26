import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1', database='testdb')
mycursor=mydb.cursor()

# Creating Table employee

mycursor.execute('create table employee(name varchar(20), salary int(20))')

# Creating Table customer

mycursor.execute("CREATE TABLE customer(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(25), address VARCHAR(55))")

# Display table

mycursor.execute('show tables')
for i in mycursor:
    print(i)


