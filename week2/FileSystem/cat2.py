import sys


def main():
    name1, *name2 = sys.argv
    for curr_file in name2:
        out = open(curr_file, 'r')
        print(out.read())
        print()
        out.close()

if __name__ == '__main__':
    main()
