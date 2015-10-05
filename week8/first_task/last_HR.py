import sqlite3
import requests
import json


def get_data_to_json(name):

    req = requests.get(name).json()
    return req


def get_all_courses_names(jsoned):
    tuples = []
    for student in jsoned:
        if len(student['courses']) == 0:
            tuples.append((student['name'], student['github'], ''))
        else:
            for course in student['courses']:
                tuples.append(
                    (student['name'], student['github'], course['name']))
    return tuples


def get_data_and_return_tuples(name):
    return get_all_courses_names(get_data_to_json(name))


def get_courses_names(tuples):
    courses = set()
    for curr_tuple in tuples:
        courses.add(curr_tuple[2])
    return courses


def get_people_names(tuples):
    people = []
    for person in tuples:
        people.append((person[0], person[1]))
    return people


def get_all_data(name):
    tuples = get_data_and_return_tuples(name)
    people = get_people_names(tuples)
    courses = get_courses_names(tuples)
    return (people, courses)


def make_tables():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    create_courses_query = '''
    CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, name TEXT)
    '''

    create_people_query = '''
    CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY,name TEXT , github TEXT)
    '''

    cursor.execute(create_courses_query)
    cursor.execute(create_people_query)

    conn.commit()

    return (conn, cursor)


def add_info_to_tables(people, courses):
    conn, cursor = make_tables()

    add_person_query = '''
    INSERT INTO people(name, github)
    VALUES
    '''

    add_courses_query = '''
    INSERT INTO courses(name)
    VALUES
    '''

    lst_courses = ["('" + course + "')" for course in courses.keys()]
    add_courses_query += ",".join(lst_courses)

    lst_people = ["('" + person[0] + "'" + ',' + "'" +
                  str(person[1]) + "')" for person in people]
    splitted_people = []
    while len(lst_people) >= 500:
        splitted_people.extend(lst_people[:500])
        lst_people = lst_people[500:]
    splitted_people.extend(lst_people)
    final_ver_query = []
    for person in splitted_people:
        final_ver_query.append(add_person_query + "".join(person))
    print(add_person_query)
    #:print(lst)
    for query in final_ver_query:
        cursor.execute(query)
    conn.commit()

    cursor.execute(add_courses_query)
    conn.commit()

    return conn, cursor


def get_from_file(filename):
    fle = open(filename)
    data = json.load(fle)

    people = []
    courses = {}

    person_id = 1
    course_id = 0

    for person in data:
        people.append((person['name'], person['github'], person_id, []))

        for course in person['courses']:
            if course['name'] in courses.keys():
                people[person_id - 1][3].append(courses[course['name']])
            else:
                course_id += 1
                courses[course['name']] = course_id
                people[person_id - 1][3].append(course_id + 1)
        person_id += 1
    return people, courses


def make_third_table(conn, cursor, people):
    make_table_query = '''
    CREATE TABLE IF NOT EXISTS connections(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES people(id),
    FOREIGN KEY(course_id) REFERENCES courses(id))
    '''

    cursor.execute(make_table_query)

    add_connection_query = '''
    INSERT INTO connections(student_id, course_id)
    VALUES
    '''
    lst_people = []
    for person in people:
        if len(person[3]) == 0:
            lst_people.append(
                "('" + str(person[2]) + "'" + ',' + str(-1) + ")")
        else:
            for con in person[3]:
                lst_people.append(
                    "('" + str(person[2]) + "'" + ',' + str(con) + ")")
    splitted_people = []
    while len(lst_people) >= 500:
        splitted_people.extend(lst_people[:500])
        lst_people = lst_people[500:]
    splitted_people.extend(lst_people)
    final_ver_query = []
    for person in splitted_people:
        final_ver_query.append(add_connection_query + "".join(person))
    for query in final_ver_query:
        cursor.execute(query)
    conn.commit()
