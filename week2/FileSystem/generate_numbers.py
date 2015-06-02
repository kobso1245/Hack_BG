import sys
from random import randint

def main():
    name1, name2, cnt = sys.argv
    out_file = open(name2, "w")
    lst = []
    for x in range(int(cnt)) :
        lst.append(str(randint(1, 1000)))

    out_file.write(" ".join(lst))
    out_file.close()
if __name__ == '__main__':
    main()