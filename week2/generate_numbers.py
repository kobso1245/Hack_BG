import sys
from random import randint

def main():
    name1, name2, cnt = sys.argv
    out_file = open(name2, "w")
    lst = []
    for x in range(int(cnt) + 1):
        lst.append(str(randint(1, 1000)))

    out_file.write(" ".join(lst))

if __name__ == '__main__':
    main()