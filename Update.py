import pymysql

con = pymysql.connect("localhost", "user", "password", "db")

cur = con.cursor()

sql = "UPDATE Personas SET nombre = 'Shirley', edad = 19 WHERE id = 14"

try:
	cur.execute(sql)
	con.commit()
	con.close()
	print("Update Succesfull!!!")
except Exception as e:
	print(e.args)