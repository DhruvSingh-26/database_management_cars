import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
cursor.execute("CREATE TABLE cars(Model_no integer(5), Model_name varchar(60), Engine_Type varchar(50), Seating_capacity integer(2), Transmission varchar(15), On_Road_Price varchar(15))")
print("TABLE CREATED")


