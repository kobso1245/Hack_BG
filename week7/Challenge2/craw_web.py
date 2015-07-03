from Crawler import *
from Histogram import *
from Plotter import *

if __name__ == '__main__':
    craw("http://register.start.bg/","histogram2")
    plot("destination_to_database_file/websites.db")
