import sqlite3
import pandas as pd

conn = sqlite3.connect("data/paysim.db")
first = True
for chunk in pd.read_csv("data/paysim.csv", chunksize=500_000):
    chunk.to_sql("transactions", conn, if_exists="replace" if first else "append", index=False)
    first = False
conn.execute("CREATE INDEX IF NOT EXISTS idx_type ON transactions(type)")
conn.execute("CREATE INDEX IF NOT EXISTS idx_orig ON transactions(nameOrig)")
conn.commit()
print(conn.execute("SELECT COUNT(*) FROM transactions").fetchone())
conn.close()
