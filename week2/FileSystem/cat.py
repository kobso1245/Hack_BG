import sys


def main():
    name1, name2 = sys.argv
    outp = open(name2, 'r')
    print(outp.read())
    outp.close()
if __name__ == '__main__':
    main()
