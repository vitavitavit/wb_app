import mysql.connector

cnx = mysql.connector.connect(user='root', password='Vitaly123!123!',
                              host='45.153.69.151',
                              database='wb_app')

cursor = cnx.cursor()

query = ("SELECT * FROM user")

cursor.execute(query)

print(query)
'''for (userid, user, password) in cursor:
    print(f"{userid}, {user}, {password}")
'''
cursor.close()
cnx.close()