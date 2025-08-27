import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="27oCt2004.",
  database="relationship_app"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Book WHERE Author = ''")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM Book ")
myresult = mycursor.fetchall()
for x in myresult:
  print(f"title: {x[1]}, author: {x[2]}")

mycursor.execute("SELECT * FROM Librarian")
myresult = mycursor.fetchall()
for x in myresult:
  print(f"name: {x[1]}, library: {x[2]}")

  