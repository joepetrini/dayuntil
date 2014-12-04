from datetime import datetime, timedelta, date
import calendar

[MON, TUE, WED, THU, FRI, SAT, SUN] = range(0, 7)
[JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC] = range(1, 13)
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

def april_fools_day(year):
    r = {'name': 'April Fools Day'}
    r['date'] = datetime(int(year), int(APR), int(1), now.hour, now.minute)
    return r


def bastille_day(year):
    r = {'name': 'Bastille Day'}
    r['date'] = datetime(int(year), int(JUL), int(14), now.hour, now.minute)
    return r


def christmas_day(year):
    d = datetime(int(year), int(DEC), int(25), now.hour, now.minute)
    r = {'name': 'Christmas'}
    r['date'] = d
    r['priority'] = 100
    return r


def christmas_eve_day(year):
    d = datetime(int(year), int(DEC), int(24), now.hour, now.minute)
    r = {'name': 'Christmas Eve'}
    r['date'] = d
    r['priority'] = 100
    return r


def cinco_de_mayo_day(year):
    r = {'name': 'Cinco de Mayo'}
    r['date'] = datetime(int(year), int(MAY), int(5), now.hour, now.minute)
    return r


def columbus_day(year):
    # 2nd Mon in Oct
    d = get_nth_day_of_month(2, MON, OCT, year)
    r = {'name': 'Columbus Day'}
    r['date'] = datetime(int(year), int(OCT), d, now.hour, now.minute)
    return r


def earth_day(year):
    r = {'name': 'Earth Day'}
    r['date'] = datetime(int(year), int(APR), int(22), now.hour, now.minute)
    return r

# EASTER

def election_day(year):
    # 1st Tues in Nov
    d = get_nth_day_of_month(1, TUE, NOV, year)
    r = {'name': 'Election Day'}
    r['date'] = datetime(int(year), int(NOV), d, now.hour, now.minute)
    return r


def fall_day(year):
    a = {2012: '9-23', 2013: '9-22', 2014: '9-23', 2015: '9-23', 2016: '9-22', 2016: '9-22', 2018: '9-23', 2019: '9-23',
         2020: '9-22'}
    d = a[year].split('-')
    r = {'name': 'Fall'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    return r


def fathers_day(year):
    # 3nd Sun in June
    d = get_nth_day_of_month(3, SUN, JUN, year)
    r = {'name': 'Father''s Day'}
    r['date'] = datetime(int(year), int(JUN), d, now.hour, now.minute)
    return r


def flag_day(year):
    r = {'name': 'Flag Day'}
    r['date'] = datetime(int(year), int(JUN), int(14), now.hour, now.minute)
    return r


def fourthofjuly_day(year):
    r = {'name': '4th of July'}
    #    r = {'name': 'Independance Day'}
    r['date'] = datetime(int(year), int(JUL), int(4), now.hour, now.minute)
    r['priority'] = 100
    return r


def groundhog_day(year):
    r = {'name': 'Groundhog Day'}
    r['date'] = datetime(int(year), int(FEB), int(2), now.hour, now.minute)
    return r


def halloween_day(year):
    r = {'name': 'Halloween'}
    r['date'] = datetime(int(year), int(10), int(31), now.hour, now.minute)
    r['priority'] = 100
    return r


def labor_day(year):
    # 1st Mon in Sep
    d = get_nth_day_of_month(1, MON, SEP, year)
    r = {'name': 'Labor Day'}
    r['date'] = datetime(int(year), int(SEP), d, now.hour, now.minute)
    return r


# TODO Lent

# TODO memorial day

def mlk_day(year):
    # 3rd Mon in Jan
    d = get_nth_day_of_month(3, MON, JAN, year)
    r = {'name': 'Martin Luther King Day'}
    r['date'] = datetime(int(year), int(JAN), d, now.hour, now.minute)
    return r


def mothers_day(year):
    # 2nd Sun in May
    d = get_nth_day_of_month(2, MON, MAY, year)
    r = {'name': 'Mother''s Day'}
    r['date'] = datetime(int(year), int(MAY), d, now.hour, now.minute)
    return r


def new_years_eve_day(year):
    r = {'name': 'New Years Eve'}
    r['date'] = datetime(int(year), int(12), int(31), now.hour, now.minute)
    r['priority'] = 100
    return r


def newyearsday_day(year):
    r = {'name': 'New Years Day'}
    r['date'] = datetime(int(year), int(1), int(1), now.hour, now.minute)
    r['priority'] = 100
    return r


def patriot_day(year):
    r = {'name': 'Patriot Day'}
    r['date'] = datetime(int(year), int(SEP), int(11), now.hour, now.minute)
    return r


def pearl_harbor_day(year):
    r = {'name': 'Pearl Harbor Day'}
    r['date'] = datetime(int(year), int(DEC), int(7), now.hour, now.minute)
    return r


def presidents_day(year):
    # 3rd Mon in Feb
    d = get_nth_day_of_month(3, MON, FEB, year)
    r = {'name': 'President''s Day'}
    r['date'] = datetime(int(year), int(FEB), d, now.hour, now.minute)
    return r


def spring_day(year):
    # a = {2012:'3-20',2013:'3-20',2014:'3-20',2015:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20'}
    #d = a[year].split('-')
    r = {'name': 'Spring'}
    r['date'] = datetime(int(year), int(MAR), int(20), now.hour, now.minute)
    r['priority'] = 100
    return r


def st_patricks_day(year):
    r = {'name': 'St Patrick''s Day'}
    r['date'] = datetime(int(year), int(MAR), int(17), now.hour, now.minute)
    r['priority'] = 100
    return r


def summer_day(year):
    a = {2012: '6-20', 2013: '6-21', 2014: '6-21', 2015: '6-21', 2016: '6-20', 2017: '6-21', 2018: '6-21', 2019: '6-21',
         2020: '6-20'}
    d = a[year].split('-')
    r = {'name': 'Summer'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    return r


# http://en.wikipedia.org/wiki/Tax_Day

def thanksgiving_day(year):
    # 4th Thursday of November
    d = get_nth_day_of_month(4, THU, NOV, year)
    r = {'name': 'Thanksgiving'}
    r['date'] = datetime(int(year), int(NOV), d, now.hour, now.minute)
    r['priority'] = 100
    return r


def three_kings_day(year):
    r = {'name':'3 Kings Day'}
    r['date'] = datetime(int(year), int(JAN), int(6), now.hour, now.minute)
    return r


def valentines_day(year):
    # Feb 14
    r = {'name': 'Valentine''s Day'}
    r['date'] = datetime(int(year), int(FEB), 14, now.hour, now.minute)
    r['priority'] = 100
    return r


def veterans_day(year):
    # Nov 11
    r = {'name': 'Veterans''s Day'}
    r['date'] = datetime(int(year), int(NOV), 11, now.hour, now.minute)
    return r


def winter_day(year):
    a = {2012: '12-21', 2013: '12-21', 2014: '12-21', 2015: '12-22', 2016: '12-21', 2017: '12-21', 2018: '12-21',
         2019: '12-22', 2020: '12-21'}
    d = a[year].split('-')
    r = {'name': 'Winter'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    return r

    # washingtons bday feb 22