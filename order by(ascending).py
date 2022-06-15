import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr=("SELECT * FROM CARS ORDER BY Model_no asc")
cursor.execute(cr)
for x in cursor:
    print(x)


