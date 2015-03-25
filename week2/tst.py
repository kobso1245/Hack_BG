def tst1():
    return tst2()
def tst2():
    return tst1()

if __name__ == '__main__':
    tst1()