import sqlite3
import pandas as pd

df = pd.read_csv('mydata.csv')
conn = sqlite3.connect('mydb.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS  mydata''')

c.execute('''
          CREATE TABLE mydata (
          id INTEGER,
          fruit VARCHAR(20),
          price INT,
          color VARCHAR(20)
          )
          ''')


df.to_sql('mydata', conn, index=False, if_exists='replace')

conn.commit()
conn.close()
