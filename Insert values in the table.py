import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="dhruv123",database="project22")
cursor=mycon.cursor()
c="INSERT INTO cars(Model_no,Model_name,Engine_Type,Seating_capacity,Transmission,On_Road_Price) VALUES(%s,%s,%s,%s,%s,%s)"
r=[(1,"Tata harrier XZA PLUS","Kryotec 2.0 L Turbocharged",5,"AUTOMATIC","24.19 lakhs"),
(2,"Tata Tigor","1.2 L Revotron",5,"AUTOMATIC","8.66 lakhs"),
(3,"Tata Altroz XZ","1.5 L Revotroq",5,"MANUAL","10.94 lakhs"),
(4,"Tata Nexon XZA Plus","1.5L Revotorq Turbocharged",5,"AUTOMATIC","15.15 lakhs"),
(5,"Tata Tigor EV XT Plus","72 V 3-Phase AC Induction Motor",5,"AUTOMATIC","10.54 lakhs"),
(6,"AUDI RS 7","Twin-Turbo 4.0-liter V-8",4,"AUTOMATIC","1.94 Cr"),
(7,"Mercedes-Benz GLC Coupe 43 AMG","4MATIC Engine",5,"AUTOMATIC","80 lakhs"),
(8,"Audi Rs 6 Avant","Twin-Turbo 4.0-liter V-8",5,"AUTOMATIC","59.42 lakhs"),
(9,"Audi Q8","3.0 L V6",5,"AUTOMATIC","1.33 Cr"),
(10,"Audi RS Q8","4.0 L V8",5,"AUTOMATIC","2.07Cr")]
cursor.executemany(c,r)
mycon.commit()	
print("ALL VALUES INSERTED") 

