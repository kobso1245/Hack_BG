from copy import deepcopy


def sum_of_divisors(n):
    return sum([x for x in range(1, n+1) if n % x == 0])


def is_prime(n):
    if n < 0:
        return False
    return sum_of_divisors(n) == n + 1


def prime_number_of_divisors(n):
    return is_prime((sum([1 for x in
                    [p for p in range(1, n+1) if n % p == 0]])))


def constains_digit(number, digit):
    return str(digit) in str(number)


def contains_digits(number, digits):
    return (0 not in [0 for x in digits if str(x) not in str(number)])


def is_number_ballanced(n):
    if n >= -9 and n <= 9:
        return True
    length = len(str(n))
    if length % 2 == 1:
        p = length // 2 + 1
    else:
        p = length // 2
    return (sum([int(x) for x in str(n)[:length//2]]) ==
            sum([int(x) for x in str(n)[p:]]))


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    result = ""
    tmp = str(n)
    for i in range(0, len(tmp)-1):
        if int(tmp[i]) == int(tmp[i + 1]):
            result = result + tmp[i] + '0'
        elif int(tmp[i]) + int(tmp[i+1]) == 10:
            result = result + tmp[i] + '0'
        else:
            result += tmp[i]
    result += tmp[-1]
    return result


def sum_matrix(m):
    return sum(map(sum, m))


def bomb_da_shet(m, pos):
    tmp = deepcopy(m)
    for row in range(len(tmp)):
        for col in range(len(tmp[0])):
            if (abs(row - pos[0]) <= 1 and abs(col - pos[1]) <= 1
                and (row != pos[0] or col != pos[1])):
                if tmp[row][col] - tmp[pos[0]][pos[1]] < 0:
                    tmp[row][col] = 0
                else:
                    tmp[row][col] -= tmp[pos[0]][pos[1]]
    return tmp


def matrix_bombing_plan(m):
    lst = [(x, y) for x in range(len(m)) for y in range(len(m[0]))]
    dct = {tpl: sum_matrix(bomb_da_shet(m, tpl)) for tpl in lst}
    min_elem = min([x for x in dct.values()])
    min_dict = {x: min_elem for x in dct.keys() if dct[x] == min_elem}
    return min_dict


def reps(input_items):
    return [x for x in input_items if input_items.count(x) != 1]


if __name__ == '__main__':
    print(reps([1, 4, 2, 6, 7, 2, 4, 11, 1, 9, 0, 2, 5, 3, 1]))
