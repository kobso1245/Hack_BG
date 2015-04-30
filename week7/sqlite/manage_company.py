import sqlite3

DATABASE = "company.db"

def make_connection(name):
    conn = sqlite3.connect(name)
    return conn.cursor()

def list_employes():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    list_query = """
    SELECT name, position FROM users
    """
    updated = cursor.execute(list_query)
    return ["{} -- {}".format(person[0], person[1]) for person in updated]

def monthly_spending():
    cursor = make_connection(DATABASE)
    spending_query = """
    SELECT monthly_salary FROM users
    """
    money = cursor.execute(spending_query)
    return sum([dolar[0] for dolar in money])

def yearly_spending():
    cursor = make_connection(DATABASE)
    yearly_bonus_query = """
    SELECT monthly_salary, year_bonus FROM users
    """
    total_money = cursor.execute(yearly_bonus_query)
    return sum([money[0] + money[1] for money in total_money])

def add_employee(data):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = """
    INSERT INTO users(name, monthly_salary, year_bonus, position)
    VALUES({}, {}, {}, {})
    """.format(data[0], data[1], data[2], data[3])

    cursor.execute(query)
    conn.commit()

if __name__ == '__main__':
    data = ['Ivo Ivo', 10000, 100000, 'CEO']
    #print(yearly_spending())
    add_employee(data)
