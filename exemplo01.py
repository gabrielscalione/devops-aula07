import sqlite3

conn = sqlite3.connect('exemplo.db')
c = conn.cursor()

c.execute('''CREATE TABLE teste(data text, qtde real)''')

c.execute('''INSERT INTO teste VALUES ('2020-09-24', 10)''')

conn.commit()
conn.close()
