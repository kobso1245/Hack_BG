from Crawler import *
from Histogram import *
from Plotter import *
import json

try:
    data = open('settings.json')
    database = json.load(data)['DATABASE']
except Exception:
    print('File settings.json not found!')


if __name__ == '__main__':
    craw("http://register.start.bg/", "histogram2")
    plot(database)
