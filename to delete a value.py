import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr="DELETE FROM cars WHERE Model_no=2"
cursor.execute(cr)
mycon.commit()
print("rows affected:",cursor.rowcount)
cursor.execute("select * from cars")
for x in cursor:
    print(x)


