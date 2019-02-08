import sqlite3
import pandas as pd

# conn = sqlite3.connect("db.db")
# dfs = pd.read_excel('data.xlsx', sheet_name=None)
# for table, df in dfs.items():
#     df.to_sql(table, conn)

# conn =sqlite3.connect("db.sqlite3")
# dfs = pd.read_excel('data.xlsx', sheet_name=None)
# for table, df in dfs.items():
#     df.to_sql(table, conn)

# cur = conn.cursor()
# cur.execute("select * from 시트1")
# rows = cur.fetchall()
# for row in rows:
#     cur.execute(f"insert into watcha_movie (title,title_en,audience,open_date,genre,watch_grade,score,poster_url,description) values({row.title},{row.title_en},{row.audience},{row.open_date},{row.genre},{row.watch_grade},{row.score},{row.poster_url},{row.description})")
#     # cur.executemany("insert into 시트1 values()",row)
#     print(row)
# conn.commit()
# conn.close()


