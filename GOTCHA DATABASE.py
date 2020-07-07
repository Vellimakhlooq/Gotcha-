import sqlite3

def database_GOTCHA():
	connection=sqlite3.connect("login_gotcha.db")

	connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL,PASSWORD TEXT)")
	connection.execute("INSERT INTO USERS VALUES(?,?)",('fahad10','pakistan'))
	connection.commit()
	result=connection.execute("SELECT * FROM USERS")
	for data in result:
		print("Username : ",data[0])
	
		print("Password : ",data[1])
	connection.close()
database_GOTCHA()