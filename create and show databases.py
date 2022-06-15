'''TO CREATE AND SHOW DATABASES'''
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123")
if mycon.is_connected()==False:
    print("error")
cursor=mycon.cursor()
cursor.execute("create database project23")
print("Database created")
cursor.execute("show databases")
for x in cursor:
    print(x)


