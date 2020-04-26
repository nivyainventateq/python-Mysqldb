import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root", password='Nivya@mysql1',database='testdb')
x=mydb.cursor()


# Limit: limit the number of records returned from the query, by using the "LIMIT" statement:
x.execute("SELECT * FROM customer LIMIT 2")

result = x.fetchall()

for x in result:
  print(x)