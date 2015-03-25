import os
import sys

def getSize(path):
    try:
        dirs = os.listdir(path)
    except FileNotFoundError as error:
        print(error)
    out_sum = 0
    for curr_dir in dirs:
        if os.path.isfile(path + '/' + curr_dir):
            out_sum += os.path.getsize(path + '/' + curr_dir)
        else:
            out_sum += getSize(path + '/' + curr_dir)
    return out_sum

if __name__ == '__main__':
    name1, name2 = sys.argv
    size = getSize(name2)
    cnt = 0
    dct = ['B','kB', 'MB', 'GB', 'TB']
    while (size / 1024) > 1:
        cnt += 1
        size /= 1024
    print("{} size is {}{}".format(name2, size, dct[cnt]))
