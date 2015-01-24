import pymysql

con = pymysql.connect("localhost", "user", "password", "db")

cur = con.cursor()

sql = "INSERT INTO Personas(nombre, edad) VALUES('hola@gmail.com', 18)"

try:
	cur.execute(sql)
	con.commit()
	con.close()
	print("Insert ok!!!")
except Exception as e:
	print(e.args)