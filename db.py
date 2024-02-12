import sqlite3

connection = sqlite3.connect('wb_db.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM goods')
goods = cursor.fetchall()

for i in goods:
    print(i)

connection.close()