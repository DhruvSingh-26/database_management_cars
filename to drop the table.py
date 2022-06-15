import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr="drop table cars"
cursor.execute(cr)
mycon.commit()
print("Table dropped")


