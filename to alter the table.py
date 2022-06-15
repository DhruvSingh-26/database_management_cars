import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cr=("ALTER TABLE CARS ADD COLUMN MILEAGE VARCHAR(30)")
cursor.execute(cr)
mycon.commit()
print("rows affected:",cursor.rowcount)


