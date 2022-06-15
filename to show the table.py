import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cursor.execute("select * from cars")
data=cursor.fetchall()
count=cursor.rowcount
print("the total no of rows retrevied from the table=",count)
for row in data:
    print(row)


