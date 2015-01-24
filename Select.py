import pymysql

con = pymysql.connect("localhost", "user", "password", "db")

cur = con.cursor()

sql = "SELECT * FROM Personas"

try:
	cur.execute(sql)
	results = cur.fetchall()
	con.close()
	for row in results:
		print(row)
except Exception as e:
	print(e.args)