from isoweek import Week


def friday_years(start, end):

    return len([x for x in range(start, end)
                if get_count(Week.weeks_of_year(x)) == 53])


def get_count(iterator):
    return sum([1 for x in iterator])

if __name__ == '__main__':
    friday_years(1900, 2015)
