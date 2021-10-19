import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
val2 = ("Jacn", "Highwayssas 21")

mycursor.execute(sql, val)
mycursor.execute(sql, val2)

mydb.commit()

print(mycursor.rowcount, "record inserted.") 