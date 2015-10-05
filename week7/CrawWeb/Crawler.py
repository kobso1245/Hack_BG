from bs4 import BeautifulSoup
import requests
import json
import sqlite3
from Histogram import Histogram


def recover_links(database):

    qlite3.connect(database)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    create_table_query = """
    CREATE TABLE IF NOT EXISTS links(url TEXT PRIMARY KEY)
    """
    cursor.execute(create_table_query)
    conn.commit()

    passed = set()

    get_passed = """
    SELECT url FROM links
    """
    req = cursor.execute(get_passed)
    conn.commit()
    data = req.fetchall()

    conn.close()
    for row in data:
        passed.add(tuple(row)[0])

    return passed


def get_links(website):

    try:
        req = requests.get(website, timeout=2)
    except Exception:
        return []
    bs = BeautifulSoup(req.text)
    all_links = []

    for link in bs.find_all('a'):
        curr_link = link.get("href")
        if not isinstance(
                curr_link,
                type(None)) and 'link.php' in curr_link:  # curr_link[:4] == 'link':
            if curr_link[:4] == 'link':
                webs = website.split('/')
                if not isinstance(webs, type(None)) and len(webs) >= 3:
                    website = webs[0] + '//' + webs[2] + '/'
                curr_link = website + curr_link
            all_links.append(curr_link)

    if website == 'http://register.start.bg':
        print("daaaaaaaaaaaaaa")
        print(all_links)

    return all_links


def save_file(save_to, hist):
    fle = open(save_to, 'w')
    json.dump(hist.get_dict(), fle)
    fle.close


def change_name(name):
    final_name = name
    if 'Apache' in name:
        return 'Apache'
    elif 'nginx' in name:
        return 'nginx'
    elif 'IIS' in name:
        return 'IIS'
    else:
        return 'other'


def make_table(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS websites(url TEXT PRIMARY KEY, server TEXT)
    """
    cursor.execute(create_table_query)
    conn.commit()


def get_histogram(all_links):
    hist = Histogram()
    our_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }

    # connections
    cnt = 0
    conn = sqlite3.connect(
        "/home/kaloyan/Documents/Hack_Bulgaria/week7/websites.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    update_query = '''
    INSERT INTO websites(url, server)
    VALUES(?, ?)
    '''

    # getting the data if any
    get_query = '''
    SELECT url FROM websites
    '''

    data = cursor.execute(get_query)
    conn.commit()
    rows = data.fetchall()
    conn.commit()
    sites = set()
    for row in rows:
        sites.add(tuple(row))

    name = ''
    adding = []
    num = 0
    equal = 0
    for link in all_links:
        equal = 0
        for i in sites:
            if link == i[0]:
                equal = 1
        if not equal:
            try:
                print(link)
                req = requests.head(link,
                                    headers=our_headers,
                                    timeout=4,
                                    allow_redirects=True)
                name = req.headers['Server']
                hist.add(change_name(name))
                adding.append((link, name,))
                cnt += 1
                if cnt == 5:
                    cursor.executemany(update_query, adding)
                    conn.commit()
                    adding = []
                    cnt = 0

            except Exception as ex:
                print(ex)
    return hist


def links(website, links_all, passed, conn, cursor):
    to_be_added = []
    curr_links = get_links(website)
    for link in curr_links:
        links_all.add(link)
        to_be_added.append(link,)
    # print(curr_links)

    if to_be_added != []:
        add_query = '''
        INSERT INTO links(url)
        VALUES(?)
        '''
        cursor.executemany(add_query, to_be_added)
        conn.commit()

    if len(curr_links) == 0:
        return []
    else:
        for link in curr_links:
            if link != website:
                print(link)
                links(link, links_all, passed, conn, cursor)


def craw(website, save_to):
    make_table("/home/kaloyan/Documents/Hack_Bulgaria/week7/websites.db")
    all_links = set()
    passed = recover_links("website.db")

    qlite3.connect("website.db")
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row

    links(website, all_links, passed, conn, cursor)
    #all_links = get_links(website)
    # print(all_links)
    hist = get_histogram(all_links)
    save_file(save_to, hist)
