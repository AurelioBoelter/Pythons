
import sqlite3

conn = sqlite3.connect('baseX.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM baseX;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
