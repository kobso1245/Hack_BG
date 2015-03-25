import sys

def main():
    name1, name2 = sys.argv
    in_file = open(name2, 'r')
    sum = 0
    lst = in_file.read()
    tmp = lst.split(' ')
    for elem in tmp:
        sum += int(elem)
    print(sum)
    in_file.close()
if __name__ == '__main__':
    main()