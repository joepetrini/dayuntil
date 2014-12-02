from datetime import datetime, timedelta, date
import calendar

MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6

JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

HAVE_30_DAYS = (APR, JUN, SEP, NOV)
HAVE_31_DAYS = (JAN, MAR, MAY, JUL, AUG, OCT, DEC)


def get_nth_day_of_month(n, weekday, month, year):
    firstday, daysinmonth = calendar.monthrange(year, month)

    # firstday is MON, weekday is WED -- start with 3rd day of month
    # firstday is WED, weekday is MON --
    # firstday = weekday
    if firstday < weekday:
        date = weekday - firstday + 1  # 2 - 0 + 1
    elif firstday > weekday:
        date = 7 - (firstday - weekday) + 1
    else:
        date = 1

    if n == 1:
        return date

    for i in range(1, n):
        date += 7
        if month in HAVE_30_DAYS and date > 30:
            raise IndexError
        if month in HAVE_31_DAYS and date > 31:
            raise IndexError
        if month == FEB and date > 28:
            ignore, daysinfeb = calendar.monthrange(year, FEB)
            if date > daysinfeb:
                raise IndexError
    return date


now = datetime.today()


def three_kings_day(year):
    return '3 Kings Day', datetime(int(year), int(JAN), int(6), now.hour, now.minute)


def april_fools_day(year):
    d = datetime(int(year), int(APR), int(1), now.hour, now.minute)
    return 'April Fools Day', d


def bastille_day(year):
    return 'Bastille Day', datetime(int(year), int(JUL), int(14), now.hour, now.minute)


def christmas_day(year):
    d = datetime(int(year), int(DEC), int(25), now.hour, now.minute)
    return 'Christmas', d


def christmas_eve_day(year):
    d = datetime(int(year), int(DEC), int(24), now.hour, now.minute)
    return 'Christmas Eve', d


def cinco_de_mayo_day(year):
    return 'Cinco de Mayo', datetime(int(year), int(MAY), int(5), now.hour, now.minute)


def columbus_day(year):
    # 2nd Mon in Oct
    d = get_nth_day_of_month(2, MON, OCT, year)
    return 'Columbus Day', datetime(int(year), int(OCT), d, now.hour, now.minute)


def earth_day(year):
    return 'Earth Day', datetime(int(year), int(APR), int(22), now.hour, now.minute)


# EASTER

def election_day(year):
    # 1st Tues in Nov
    d = get_nth_day_of_month(1, TUE, NOV, year)
    return 'Election Day', datetime(int(year), int(NOV), d, now.hour, now.minute)


def fall_day(year):
    a = {2012: '9-23', 2013: '9-22', 2014: '9-23', 2015: '9-23', 2016: '9-22', 2016: '9-22', 2018: '9-23', 2019: '9-23',
         2020: '9-22'}
    d = a[year].split('-')
    return 'Fall', datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)


def fathers_day(year):
    # 3nd Sun in June
    d = get_nth_day_of_month(3, SUN, JUN, year)
    return 'Father''s Day', datetime(int(year), int(JUN), d, now.hour, now.minute)


def flag_day(year):
    return 'Flag Day', datetime(int(year), int(JUN), int(14), now.hour, now.minute)


def fourthofjuly_day(year):
    return 'the 4th of July', datetime(int(year), int(JUL), int(4), now.hour, now.minute)


def fourth_of_july_day(year):
    return 'the 4th of July', datetime(int(year), int(JUL), int(4), now.hour, now.minute)


def groundhog_day(year):
    return 'Groundhog Day', datetime(int(year), int(FEB), int(2), now.hour, now.minute)


def halloween_day(year):
    return 'Halloween', datetime(int(year), int(10), int(31), now.hour, now.minute)


def independance_day(year):
    return 'Independance Day', datetime(int(year), int(JUL), int(4), now.hour, now.minute)


def labor_day(year):
    # 1st Mon in Sep
    d = get_nth_day_of_month(1, MON, SEP, year)
    return 'Labor Day', datetime(int(year), int(SEP), d, now.hour, now.minute)


# TODO Lent

# TODO memorial day

def mlk_day(year):
    # 3rd Mon in Jan
    d = get_nth_day_of_month(3, MON, JAN, year)
    return 'Martin Luther King Day', datetime(int(year), int(JAN), d, now.hour, now.minute)


def mothers_day(year):
    # 2nd Sun in May
    d = get_nth_day_of_month(2, MON, MAY, year)
    return 'Mother''s Day', datetime(int(year), int(MAY), d, now.hour, now.minute)


def new_years_eve_day(year):
    return 'New Years Eve', datetime(int(year), int(12), int(31), now.hour, now.minute)


def newyearseve_day(year):
    return 'New Years Eve', datetime(int(year), int(12), int(31), now.hour, now.minute)


def newyearseve_day(year):
    return 'New Years Eve', datetime(int(year), int(12), int(31), now.hour, now.minute)


def newyearsday_day(year):
    return 'New Years Day', datetime(int(year), int(1), int(1), now.hour, now.minute)


def new_years_day_day(year):
    return 'New Years Day', datetime(int(year), int(1), int(1), now.hour, now.minute)


def patriot_day(year):
    return 'Patriot Day', datetime(int(year), int(SEP), int(11), now.hour, now.minute)


def pearl_harbor_day(year):
    return 'Pearl Harbor Day', datetime(int(year), int(DEC), int(7), now.hour, now.minute)


def presidents_day(year):
    # 3rd Mon in Feb
    d = get_nth_day_of_month(3, MON, FEB, year)
    return 'President''s Day', datetime(int(year), int(FEB), d, now.hour, now.minute)


def spring_day(year):
    # a = {2012:'3-20',2013:'3-20',2014:'3-20',2015:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20'}
    #d = a[year].split('-')
    return 'Spring', datetime(int(year), int(MAR), int(20), now.hour, now.minute)


def st_patricks_day(year):
    return 'St Patrick''s Day', datetime(int(year), int(MAR), int(17), now.hour, now.minute)


def summer_day(year):
    a = {2012: '6-20', 2013: '6-21', 2014: '6-21', 2015: '6-21', 2016: '6-20', 2017: '6-21', 2018: '6-21', 2019: '6-21',
         2020: '6-20'}
    d = a[year].split('-')
    return 'Summer', datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)


# http://en.wikipedia.org/wiki/Tax_Day

def thanksgiving_day(year):
    # 4th Thursday of November
    d = get_nth_day_of_month(4, THU, NOV, year)
    return 'Thanksgiving', datetime(int(year), int(NOV), d, now.hour, now.minute)


def valentines_day(year):
    # Feb 14
    return 'Valentine''s Day', datetime(int(year), int(FEB), 14, now.hour, now.minute)


def veterans_day(year):
    # Nov 11
    return 'Veterans''s Day', datetime(int(year), int(NOV), 11, now.hour, now.minute)


def winter_day(year):
    a = {2012: '12-21', 2013: '12-21', 2014: '12-21', 2015: '12-22', 2016: '12-21', 2017: '12-21', 2018: '12-21',
         2019: '12-22', 2020: '12-21'}
    d = a[year].split('-')
    return 'Winter', datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)


def xmas_day(year):
    d = datetime(int(year), int(DEC), int(25), now.hour, now.minute)
    return 'xmas', d


    # washingtons bday feb 22