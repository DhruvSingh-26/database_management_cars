import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr="UPDATE cars SET Model_name='{}' WHERE Model_name='{}'".format("BMW X5","Tata Altroz XZ")
cursor.execute(cr)
mycon.commit()
print("rows affected:",cursor.rowcount)


