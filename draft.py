import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()
conn.close()