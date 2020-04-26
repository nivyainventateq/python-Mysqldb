import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1')
mycursor=mydb.cursor()

# Creating Database

mycursor.execute("create database testdb")

# display databases

mycursor.execute("show databases")
for db in mycursor:
    print(db)