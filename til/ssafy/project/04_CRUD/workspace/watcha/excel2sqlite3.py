import sqlite3
import pandas as pd

conn = sqlite3.connect("db.sqlite3")
dfs = pd.read_excel('data.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql("insert_data", conn)


cur = conn.cursor()
cur.execute("select * from insert_data")
rows = cur.fetchall()
for row in rows:
    cur.execute("insert into watchlist_movie (title,title_en,audience,open_date,genre,watch_grade,score,poster_url,description) values(?,?,?,?,?,?,?,?,?);",(row[1],row[2],row[3],row[4][0:11:1],row[5],row[6],row[7],row[8],row[9]))
    # cur.executemany("insert into 시트1 values()",row)
    print(row[4][0:11:1])
conn.commit()
conn.close()


