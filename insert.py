import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Nivya@mysql1', database='testdb')
mycursor=mydb.cursor()

# Inserting values to the existing Table

# enter="Insert into employee(name,salary) values(%s,%s)"
# data=[('Arun',25000),('Varun',45000),('Tarun',48000)]
# mycursor.executemany(enter,data)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# customer table

sql = "INSERT INTO customer(name, address) VALUES (%s, %s)"
val = [ ('tonny','delhi'),('dolly','mumbai'),('sheety','karnataka')]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("1 record inserted, ID:", mycursor.lastrowid)
print(mycursor.lastrowid)


#  inserting only one row to a existing table

# x="INSERT INTO employee VALUES('raj',33400)"
# mycursor.execute(x)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)
