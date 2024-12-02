import mysql.connector
from utilities.configurations import *
# host, database, user, password
conn = get_connection()
print(conn.is_connected())
# print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
# rowAll = cursor.fetchall()
# print(rowAll)

rows = cursor.fetchall()
print(type(rows))
print(rows)
suma = 0
for row in rows:
    suma = suma + row[2]
print(suma)
assert suma == 361

# query = "update customerInfo set Location = %s where CourseName = %s"
# data = ("UK", "Jmeter")
# cursor.execute(query, data)
# conn.commit()
# conn.close()
