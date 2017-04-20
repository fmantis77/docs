import sqlite3 as sql
con=sql.connect(':memory:')
con.execute("create table essai(a char(10));")
con.commit()

