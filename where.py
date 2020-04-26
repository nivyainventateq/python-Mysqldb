import mysql.connector
mydb=mysql.connector.connect(host='localhost',user="root", password='Nivya@mysql1',database='testdb')
x=mydb.cursor()

# where  clause

x.execute("select  * from customers where address='Lowstreet 4'")
result=x.fetchall()
for i in result:
    print(i)

# like % %

x.execute("SELECT * FROM customers WHERE address LIKE '%st%'")
# x.execute("SELECT * FROM customers WHERE address = '%r'")
result=x.fetchall()
for i in result:
    print(i)


