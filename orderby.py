import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root", password='Nivya@mysql1',database='testdb')
x=mydb.cursor()

# order by to sort the result

sql = "SELECT * FROM customer ORDER BY id"
x.execute(sql)

result =x.fetchall()
for i in result:
  print(i)

#order by desc

sql = "SELECT * FROM customer ORDER BY id ASC"
x.execute(sql)

result =x.fetchall()
for i in result:
  print(i)

# order by asc

sql = "SELECT * FROM employee ORDER BY salary"
x.execute(sql)

result =x.fetchall()
for i in result:
  print(i)