from bs4 import BeautifulSoup
import requests
import json
from Histogram import Histogram

def craw(website, save_to):
    req = requests.get(website)
    bs = BeautifulSoup(req.text)
    all_links = []
    for link in bs.find_all('a'):
        curr_link = link.get("href")
        if  type(curr_link) is not type(None) and  curr_link[:4] == 'link':
            curr_link = "http://register.start.bg/" + curr_link
        all_links.append(curr_link)

    hist = Histogram()

    our_headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
             }
    for link in all_links:
        try:
            print(link)
            req = requests.head(link, headers=our_headers,timeout=2, allow_redirects=True)
            name = req.headers['Server']
            print(name)
            final_name = name
            if 'Apache' in name:
                final_name = 'Apache'
            elif 'nginx' in name:
                final_name = 'nginx'
            elif 'IIS' in name:
                final_name = 'IIS'
            else:
                final_name = name
            hist.add(final_name)
        except Exception:
            print("Exception found!")

    print(hist.get_dict())

    fle = open(save_to, 'w')
    json.dump(hist.get_dict(), fle)
    fle.close()
