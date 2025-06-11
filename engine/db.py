import sqlite3

connection=sqlite3.connect("jarvis.db")
cursor=connection.cursor()

query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)

query="INSERT INTO sys_command VALUES (null, 'vs', 'C:\\Users\\Kushal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')"
cursor.execute(query)
connection.commit()

# query="DELETE FROM sys_command WHERE name = ?"
# cursor.execute(query, ('vscode',))
# connection.commit()

query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
cursor.execute(query)

query="INSERT INTO web_command VALUES (null, 'google', 'https://www.google.com/')"
cursor.execute(query)
connection.commit()

# query="DELETE FROM web_command WHERE name = ?"
# cursor.execute(query, ('Youtube',))
# connection.commit()

# Test usage
# app_name="canva"
# cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
# results=cursor.fetchall()
# print(results)
# print(results[0])
# print(results[0][0])