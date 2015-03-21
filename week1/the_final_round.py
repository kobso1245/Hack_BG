THE_ANSWER_OF_EVERYTHING = 42
import calendar
from math import log

def count_words(input_strings):
    return {name: input_strings.count(name) for name in input_strings}


def unique_words_count(arr):
    return sum([1 for elem in set(arr)])


def nan_expand(times):
    if times == 0:
        return ""
    if times == 1:
        return "Not a NaN"
    else:
        return "Not a " + nan_expand(times - 1)


def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    if "Not a NaN" not in expanded or len(expanded) != len("Not a NaN"):
        return False
    else:
        return expanded.count("Not a")


'''def prime_factorization(n):
     primes = [] '''

# tova e mnooooooooogo losho, aspirin needed


def group(things):
    result = []
    tmp = []
    for i in range(1, len(things)):
        tmp.append(things[i - 1])
        if things[i - 1] != things[i]:
            result.append(tmp)
            tmp = []
    tmp.append(things[-1])
    if tmp != []:
        result.append(tmp)
    return result


def max_consecutive(items):
    return max([len(lst) for lst in group(items)])


def groupby(func, seq):
    return{result: [elem for elem in seq
           if func(elem) == result] for result
           in set([func(elem) for elem in seq])}


def is_an_bn(word):
    if word == "":
        return True
    tmp = group(list(word))
    if len(tmp) == 2 and len(tmp[0]) == len(tmp[1]) and tmp[0][0] == 'a':
        return True
    else:
        return False


def doubler(n, poss):
    if poss % 2 == 0:
        poss = poss + 1
        return n
    else:
        if 2*n < 10:
            poss += 1
            return 2*n
        else:
            poss += 1
            return (((2*n) % 10) + ((2*n) // 10))


def is_credit_card_valid(number):
    pos = 0
    result = []
    casted = str(number)
    for i in range(0, len(casted)):
        result.append(doubler(int(casted[i]), pos))
        pos += 1
    return sum(result) % 10 == 0


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    return [(x, n - x) for x in range(2, n//2 + 1)
            if is_prime(x) and is_prime(n - x)]


def main_diag_and_scnd_diag(matr):
    length = len(matr)
    sum_main = 0
    sum_sec = 0
    for i in range(length):
        sum_main += matr[i][i]
        sum_sec += matr[i][length - 1]
    return (sum_main == sum_sec, sum_main)


def magic_square(matr):
    length = len(matr)
    cols = [sum([matr[i][j] for i in range(length)]) for j in range(length)]
    cols.extend([sum([matr[i][i] for i in range(length)]),
                sum([matr[i][length-i-1] for i in range(length)])])
    cols.extend([sum(row) for row in matr])
    return len(set(cols)) == 1


def next_prime(n):
    while THE_ANSWER_OF_EVERYTHING == 42:
        n += 1
        if is_prime(n):
            return n


def times_div(n, div):
    cnt = 0
    while div <= n and n % div == 0:
        cnt += 1
        n //= div
    return cnt


def prime_factorization(n):
    div = 2
    result = []
    while n > 1:
        times = times_div(n, div)
        n //= (div ** times)
        if times != 0:
            result.append((div, times))
        div = next_prime(div)
    return result


def reduce_file_path(path):
    splitted = path.split('/')
    while '.' in splitted:
        splitted.remove('.')

    while '' in splitted:
        splitted.remove('')
    output = []
    while len(splitted) != 0:
        top = splitted.pop(0)
        if top == '..':
            if len(output) != 0:
                output.pop()
        else:
            output.append(top)
    return "/"+"/".join(output)


def is_leap_year(year):
    if calendar.isleap(year):
        return {3, 4}
    else:
        return {4}


def friday_years(start, end):
    return sum([1 for elem in[year for year in range(start, end + 1)
               if calendar.weekday(year, 1, 1) in is_leap_year(year)]])

if __name__ == '__main__':
    print(friday_years(1990, 2015))
