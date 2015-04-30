import sqlite3

create_table_query = """
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, monthly_salary int, year_bonus int, position TEXT)
"""

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute(create_table_query)


#insert query

insert_into_table_query = """
INSERT INTO users(name, monthly_salary, year_bonus, position)
VALUES("Ivan Ivanov", 5000, 10000, "Software Developer"),
      ("Rado Rado", 500, 0, "Technical Support Intern")
"""

cursor.execute(insert_into_table_query)
conn.commit()
