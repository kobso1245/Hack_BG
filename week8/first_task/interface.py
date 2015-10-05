import sqlite3


def make_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor


def make_query(name):
    conn, cursor = make_connection()

    if name == 'courses':
        get_courses_query = '''
        SELECT name FROM {}
        '''.format(name)
    else:
        get_courses_query = '''
        SELECT name, github FROM {}
        '''.format(name)

    data = cursor.execute(get_courses_query)
    data = data.fetchall()
    conn.commit()
    conn.close()
    if name == 'courses':
        names = [row['name'] for row in data]
    else:
        names = [(row['name'], row['github']) for row in data]

    return names


def get_students():
    return make_query('people')


def get_courses():
    return make_query('courses')


def get_all_students_with_their_courses():
    conn, cursor = make_connection()

    get_query = '''
    SELECT people.name, courses.name AS ime
    FROM people
    JOIN courses
    JOIN connections
    ON connections.student_id = people.id AND connections.course_id = courses.id
    '''

    people = cursor.execute(get_query).fetchall()
    print(people[0].keys())
    return [(person['name'], person['ime'])for person in people]


def get_max_count(ids):
    lst = [(elem, ids.count(elem)) for elem in ids]
    elems = set(lst)
    cnt = lst[0][1]
    elem_max = lst[0][0]
    for elem in elems:
        if elem[1] != -1:
            if elem[1] >= cnt:
                cnt = elem[1]
                elem_max = elem[0]

    return elem_max


def get_student_name_from_id(conn, cursor, student_id):
    get_student_query = '''
    SELECT name, github FROM people
    WHERE id = {}
    '''.format(student_id)

    data = cursor.execute(get_student_query).fetchone()
    conn.commit()
    return data['name'], data['github']
    conn.close()


def get_student_with_most_courses():
    conn, cursor = make_connection()

    get_all_student_ids_query = '''
    SELECT student_id FROM connections
    '''
    data = cursor.execute(get_all_student_ids_query)
    data = data.fetchall()
    ids = [row['student_id'] for row in data]

    max_elem = get_max_count(ids)
    return get_student_name_from_id(conn, cursor, max_elem)
