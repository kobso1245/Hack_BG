def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def nth_fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n > 2:
        out_lst = [1, 1]
        while n > 2:
            out_lst.append(out_lst[-1] + out_lst[-2])
            n -= 1
        return out_lst


def sum_all_digs(n):
    sum_dg = 0
    while n != 0:
        sum_dg += n % 10
        n = n // 10
    return sum_dg


def fact_digits(n):
    sum_fac_dg = 0
    while n != 0:
        sum_fac_dg += factorial(n % 10)
        n = n // 10
    return sum_fac_dg


def pallindrome(n):
    return str(n)[::-1] == str(n)


def to_digits(n):
    exit_list = []
    while n != 0:
        exit_list += [n % 10]
        n = n // 10
    return exit_list[::-1]


def next_hack(n):
    nxt = n + 1
    while nxt:
        if pallindrome(bin(nxt)[2:]) and str(bin(nxt)[2:]).count('1') % 2 != 0:
            return nxt
        else:
            nxt += 1


def to_number(lst):
    out = 0
    for elem in lst:
        out = out * 10 + int(elem)
    return out


def fib_number(n):
    lst = nth_fib(n)
    out_lst = []
    tmp = []
    for elem in lst:
        tmp = []
        if elem >= 10:
            while elem != 0:
                tmp.append(elem % 10)
                elem = elem // 10
            out_lst += tmp[::-1]
        else:
            out_lst.append(elem)
    return to_number(out_lst)


def count_vowels(str):
    vowels = "aeiouy"
    cnt = 0
    form_str = str.lower()
    for item in form_str:
        for letter in vowels:
            if letter == item:
                cnt += 1
    return cnt


def count_con(str):
    vowels = "bcdfghjklmnpqrstvwxz"
    cnt = 0
    form_str = str.lower()
    for item in form_str:
        for letter in vowels:
            if letter == item:
                cnt += 1
    return cnt


def char_histogram(str1):
    out_dic = {}
    for elem in str1:
        out_dic[elem] = str1.count(elem)
    return out_dic


def rev(n):
    out_num = 0
    while n != 0:
        out_num = out_num*10 + n % 10
        n = n // 10
    return out_num


def p_score(n):
    if pallindrome(n):
        return 1
    else:
        return 1 + p_score(n + rev(n))


def is_increasing(seq):
    for i in range(0, len(seq)-1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(0, len(seq)-1):
        if seq[i] > seq[i + 1]:
            return True
    return False
