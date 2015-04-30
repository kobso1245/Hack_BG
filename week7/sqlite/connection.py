import sqlite3

conn = sqlite3.connect("polyglot.db")
cursor = conn.cursor()

cursor.execute("UPDATE languages SET answered = 1 WHERE language = 'Go'")

result = cursor.execute("SELECT language, answered FROM languages")

for row in result:
    print(row)
