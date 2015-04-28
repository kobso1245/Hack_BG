import matplotlib.pyplot as plt
import numpy as np
import json
def plot(filename):
    fl = open(filename)
    jsoned = json.load(fl)
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Apache', 'IIS', 'nginx', 'other'
    total_cnt = 0
    for elem in jsoned.keys():
        total_cnt += jsoned[elem]
    apache = jsoned['Apache']/total_cnt
    iis = jsoned['IIS']/total_cnt
    nginx = jsoned['nginx']/total_cnt
    other = (1 - apache - iis - nginx)
    sizes = [apache, iis, nginx, other]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()
