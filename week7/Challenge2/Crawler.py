from bs4 import BeautifulSoup
import requests
import json
import sqlite3
from Histogram import Histogram


def get_links(website):
    try:
        req = requests.get(website)
    except Exception:
        return []
    bs = BeautifulSoup(req.text)
    all_links = []
    for link in bs.find_all('a'):
        curr_link = link.get("href")
        if type(curr_link) is not type(None) and  curr_link[:4] == 'link':
            curr_link = website  + curr_link
            all_links.append(curr_link)

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


    #connections
    cnt = 0
    conn = sqlite3.connect("/home/kaloyan/Documents/Hack_Bulgaria/week7/websites.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    update_query = '''
    INSERT INTO websites(url, server)
    VALUES(?, ?)
    '''

    #getting the data if any
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


def links(website):
    curr_links = get_links(website)
    if len(curr_links) == 0:
        return [] 
    else:
        for link in curr_links:
            return curr_links + links(link)

def craw(website, save_to):
    make_table("/home/kaloyan/Documents/Hack_Bulgaria/week7/websites.db")
    all_links = []
    all_links = links(website)
    #all_links = get_links(website)
    print(all_links)
    hist = get_histogram(all_links)
    save_file(save_to, hist)
