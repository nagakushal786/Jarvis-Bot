import sqlite3
import csv

connection=sqlite3.connect("jarvis.db")
cursor=connection.cursor()

# SYSTEM TABLE
query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null, 'vs', 'C:\\Users\\Kushal\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')"
# cursor.execute(query)
# connection.commit()

# query="DELETE FROM sys_command WHERE name = ?"
# cursor.execute(query, ('vscode',))
# connection.commit()



# WEB COMMANDS TABLE
query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
cursor.execute(query)

# query="INSERT INTO web_command VALUES (null, 'google', 'https://www.google.com/')"
# cursor.execute(query)
# connection.commit()

# query="DELETE FROM web_command WHERE name = ?"
# cursor.execute(query, ('Youtube',))
# connection.commit()



# CONTACTS TABLE
query="CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)"
cursor.execute(query)

# desired_columns_idx=[0, 20]
# with open('contacts.csv', 'r', encoding='utf-8') as csv_file:
#   csv_reader=csv.reader(csv_file)
#   for row in csv_reader:
#     name=row[0].lower()
#     mobile=row[20]
#     selected_data=[name, mobile]
#     temp_query="INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?)"
#     cursor.execute(temp_query, tuple(selected_data))
# connection.commit()
# connection.close()

# query="DELETE FROM contacts WHERE name is NULL OR TRIM(name)=''"
# cursor.execute(query)
# connection.commit()

# query="DELETE FROM contacts WHERE id NOT IN (SELECT MIN(id) FROM contacts GROUP BY name)"
# cursor.execute(query)
# connection.commit()

# query="DELETE FROM contacts"
# cursor.execute(query)
# connection.commit()

# query='moksha'
# query=query.strip().lower()
# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%'+query+'%', query+'%'))
# results=cursor.fetchall()
# print(results[0][0])



# Test usage
# app_name="canva"
# cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
# results=cursor.fetchall()
# print(results)
# print(results[0])
# print(results[0][0])