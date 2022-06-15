import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr=("SELECT Model_name,count(*) FROM CARS GROUP BY Model_name")
cursor.execute(cr)
for x in cursor:
    print(x)


