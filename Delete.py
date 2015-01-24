import pymysql

con = pymysql.connect("localhost", "user", "password", "db")

cur = con.cursor()

sql = "DELETE FROM Personas WHERE nombre = 'Steve'"

try:
	cur.execute(sql)
	con.commit()
	con.close()
	print("Delete ok!!!")
except Exception as e:
	print(e.args)