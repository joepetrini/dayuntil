from datetime import datetime, timedelta, date
from dateutil.easter import easter
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
    r['desc'] = 'April Fools Day is celebrated every year on the first day of April'
    r['alt_names'] = 'all-fools-day'
    r['link'] = 'http://en.wikipedia.org/wiki/April_Fools%27_Day'
    r['link_title'] = 'Wikipedia'
    return r


def bastille_day(year):
    r = {'name': 'Bastille Day'}
    r['date'] = datetime(int(year), int(JUL), int(14), now.hour, now.minute)
    r['desc'] = 'Bastille Day, also called French National Day, is celebrated on July 14th each year.'
    r['alt_names'] = 'french-national-day'
    r['link'] = 'http://en.wikipedia.org/wiki/Bastille_Day'
    r['link_title'] = 'Wikipedia'
    return r


def christmas_day(year):
    d = datetime(int(year), int(DEC), int(25), now.hour, now.minute)
    r = {'name': 'Christmas'}
    r['date'] = d
    r['priority'] = 100
    r['desc'] = 'Christmas is celebration of the birth of Jesus Christ observed on December 25 each year.'
    r['alt_names'] = 'xmas'
    r['link'] = 'http://en.wikipedia.org/wiki/Christmas'
    r['link_title'] = 'Wikipedia'
    return r


def christmas_eve_day(year):
    d = datetime(int(year), int(DEC), int(24), now.hour, now.minute)
    r = {'name': 'Christmas Eve'}
    r['date'] = d
    r['priority'] = 100
    r['desc'] = 'Christmas Eve is the evening or day before Christmas Day.  It occurs on December 24.'
    r['alt_names'] = 'xmas-eve'
    r['link'] = 'http://en.wikipedia.org/wiki/Christmas_Eve'
    r['link_title'] = 'Wikipedia'
    return r


def cinco_de_mayo_day(year):
    r = {'name': 'Cinco de Mayo'}
    r['date'] = datetime(int(year), int(MAY), int(5), now.hour, now.minute)
    r['desc'] = """
            Cinco de Mayo (Spanish for "fifth of May") is a celebration held on May 5.
            It honors the Mexican army's unlikely victory over French forces at the Battle of Puebla.
            """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Cinco_de_Mayo'
    r['link_title'] = 'Wikipedia'
    return r


def columbus_day(year):
    # 2nd Mon in Oct
    d = get_nth_day_of_month(2, MON, OCT, year)
    r = {'name': 'Columbus Day'}
    r['date'] = datetime(int(year), int(OCT), d, now.hour, now.minute)
    r['desc'] = """
                Celebration of the anniversary of Christopher Columbus's arrival in the Americas, which happened on October 12, 1492.
                It is observed on the 2nd Monday of October.
                """
    r['alt_names'] = 'discovery-day'
    r['link'] = 'http://en.wikipedia.org/wiki/Columbus_Day'
    r['link_title'] = 'Wikipedia'
    return r


def earth_day(year):
    r = {'name': 'Earth Day'}
    r['date'] = datetime(int(year), int(APR), int(22), now.hour, now.minute)
    r['desc'] = """
                Earth Day has been celebrated on April 22 since 1970.
                Events are held world wide to demonstrate support for environmental protection.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Earth_Day'
    r['link_title'] = 'Wikipedia'
    return r


def easter_day(year):
    d = easter(year)
    r = {'name': 'Easter'}
    r['date'] = datetime(int(year), int(MAR), d.day, now.hour, now.minute)
    r['desc'] = """
                Easter or Resurrection Sunday is a festival and holiday celebrating the Resurrection of Jesus Christ
                from the dead, which occurred three days after his crucifixion.
                """
    r['alt_names'] = 'resurrection-sunday'
    r['link'] = 'http://en.wikipedia.org/wiki/Easter'
    r['link_title'] = 'Wikipedia'
    return r


def election_day(year):
    # 1st Tues after the first monday in Nov
    d = get_nth_day_of_month(1, TUE, NOV, year)
    if d == 1:
        d = 8
    r = {'name': 'Election Day'}
    r['date'] = datetime(int(year), int(NOV), d, now.hour, now.minute)
    r['desc'] = """
                Election Day in the United States is the day set by law for the general elections of public officials.
                It occurs on the Tuesday right after the first Monday in November
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Election_Day_%28United_States%29'
    r['link_title'] = 'Wikipedia'
    return r


def fall_day(year):
    a = {2012: '9-23', 2013: '9-22', 2014: '9-23', 2015: '9-23', 2016: '9-22', 2016: '9-22', 2018: '9-23', 2019: '9-23',
         2020: '9-22'}
    d = a[year].split('-')
    r = {'name': 'Fall'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Fall, in the Northern Hemisphere, is the period between the autumnal equinox
                and the winter solstice.
                """
    r['alt_names'] = 'autumn'
    r['link'] = 'http://en.wikipedia.org/wiki/Autumn'
    r['link_title'] = 'Wikipedia'
    return r


def fathers_day(year):
    # 3nd Sun in June
    d = get_nth_day_of_month(3, SUN, JUN, year)
    r = {'name': 'Father''s Day'}
    r['date'] = datetime(int(year), int(JUN), d, now.hour, now.minute)
    r['desc'] = """
                Father's Day is a celebration honoring fathers and celebrating fatherhood,
                paternal bonds, and the influence of fathers in society.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Father%27s_Day'
    r['link_title'] = 'Wikipedia'
    return r


def flag_day(year):
    r = {'name': 'Flag Day'}
    r['date'] = datetime(int(year), int(JUN), int(14), now.hour, now.minute)
    r['desc'] = """
                In the United States, Flag Day is celebrated on June 14.
                It commemorates the adoption of the flag of the United States, which happened on that day in 1777.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Flag_Day_%28United_States%29'
    r['link_title'] = 'Wikipedia'
    return r


def fourthofjuly_day(year):
    r = {'name': '4th of July'}
    #    r = {'name': 'Independance Day'}
    r['date'] = datetime(int(year), int(JUL), int(4), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Independence Day, commonly known as the Fourth of July,
                is a federal holiday in the US commemorating the adoption of the Declaration
                of Independence on July 4, 1776.
                """
    r['alt_names'] = 'independance-day'
    r['link'] = 'http://en.wikipedia.org/wiki/Independence_Day_%28United_States%29'
    r['link_title'] = 'Wikipedia'
    return r


def groundhog_day(year):
    r = {'name': 'Groundhog Day'}
    r['date'] = datetime(int(year), int(FEB), int(2), now.hour, now.minute)
    r['desc'] = """
                Groundhog Day is a day celebrated on February 2. According to folklore,
                if it is cloudy when a groundhog emerges from its burrow on this day,
                then spring will come early.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Groundhog_Day'
    r['link_title'] = 'Wikipedia'
    return r


def halloween_day(year):
    r = {'name': 'Halloween'}
    r['date'] = datetime(int(year), int(10), int(31), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Halloween is a yearly celebration observed in a number of countries on 31 October.
                The word "Halloween" means "hallowed evening" or "holy evening".
                """
    r['alt_names'] = 'all-hallows-eve'
    r['link'] = 'http://en.wikipedia.org/wiki/Halloween'
    r['link_title'] = 'Wikipedia'
    return r


def labor_day(year):
    # 1st Mon in Sep
    d = get_nth_day_of_month(1, MON, SEP, year)
    r = {'name': 'Labor Day'}
    r['date'] = datetime(int(year), int(SEP), d, now.hour, now.minute)
    r['desc'] = """
                Labor Day in the United States is a holiday celebrated on the first Monday in September.
                It is a celebration of the American labor movement and is dedicated to the social and
                economic achievements of workers.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Labor_Day'
    r['link_title'] = 'Wikipedia'
    return r


# TODO Lent

# TODO memorial day

def mlk_day(year):
    # 3rd Mon in Jan
    d = get_nth_day_of_month(3, MON, JAN, year)
    r = {'name': 'MLK Day'}
    r['date'] = datetime(int(year), int(JAN), d, now.hour, now.minute)
    r['desc'] = """
                Martin Luther King, Jr. Day is an American federal holiday marking his birthday.
                It is observed on the third Monday of January each year,
                which is around the time of King's birthday, January 15.
                """
    r['alt_names'] = 'martin-luther-king-jr-day'
    r['link'] = 'http://en.wikipedia.org/wiki/Martin_Luther_King,_Jr._Day'
    r['link_title'] = 'Wikipedia'
    return r


def mothers_day(year):
    # 2nd Sun in May
    d = get_nth_day_of_month(2, MON, MAY, year)
    r = {'name': 'Mother''s Day'}
    r['date'] = datetime(int(year), int(MAY), d, now.hour, now.minute)
    r['desc'] = """
                Mother's Day is a modern celebration originating in North America,
                honoring one's own mother, as well as motherhood, maternal bonds,
                and the influence of mothers in society.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Mother%27s_Day'
    r['link_title'] = 'Wikipedia'
    return r


def new_years_eve_day(year):
    r = {'name': 'New Years Eve'}
    r['date'] = datetime(int(year), int(12), int(31), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                New Year's Eve, is the last day of the year on December 31.
                """
    r['alt_names'] = 'old-years-day'
    r['link'] = 'http://en.wikipedia.org/wiki/New_Year%27s_Eve'
    r['link_title'] = 'Wikipedia'
    return r


def newyearsday_day(year):
    r = {'name': 'New Years Day'}
    r['date'] = datetime(int(year), int(1), int(1), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                New Year's Day is observed on January 1, the first day of the year on the modern Gregorian calendar.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/New_Year%27s_Day'
    r['link_title'] = 'Wikipedia'
    return r


def patriot_day(year):
    r = {'name': 'Patriot Day'}
    r['date'] = datetime(int(year), int(SEP), int(11), now.hour, now.minute)
    r['desc'] = """
                In the United States, Patriot Day observed as the National Day of Service and Remembrance,
                occurs on September 11 in memory of those killed in the 2001 September 11 attacks.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Patriot_Day'
    r['link_title'] = 'Wikipedia'
    return r


def pearl_harbor_day(year):
    r = {'name': 'Pearl Harbor Day'}
    r['date'] = datetime(int(year), int(DEC), int(7), now.hour, now.minute)
    r['desc'] = ''
    r['alt_names'] = ''
    r['link'] = ''
    r['link_title'] = ''
    return r


def presidents_day(year):
    # 3rd Mon in Feb
    d = get_nth_day_of_month(3, MON, FEB, year)
    r = {'name': 'President''s Day'}
    r['date'] = datetime(int(year), int(FEB), d, now.hour, now.minute)
    r['desc'] = """
                National Pearl Harbor Remembrance Day, which is observed annually on December 7,
                is to remember and honor all those who died in the attack on Pearl Harbor on December 7, 1941.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/National_Pearl_Harbor_Remembrance_Day'
    r['link_title'] = 'Wikipedia'
    return r


def spring_day(year):
    # a = {2012:'3-20',2013:'3-20',2014:'3-20',2015:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20',2016:'3-20'}
    #d = a[year].split('-')
    r = {'name': 'Spring'}
    r['date'] = datetime(int(year), int(MAR), int(20), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = 'The first day of Spring also know as the March equinox'
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/March_equinox'
    r['link_title'] = 'Wikipedia'
    return r


def st_patricks_day(year):
    r = {'name': 'St Patrick''s Day'}
    r['date'] = datetime(int(year), int(MAR), int(17), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Saint Patrick's Day, or the Feast of Saint Patrick,
                is a cultural and religious celebration occurring annually on 17 March,
                the death date of the most commonly-recognised patron saint of Ireland.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Saint_Patrick%27s_Day'
    r['link_title'] = 'Wikipedia'
    return r


def summer_day(year):
    a = {2012: '6-20', 2013: '6-21', 2014: '6-21', 2015: '6-21', 2016: '6-20', 2017: '6-21', 2018: '6-21', 2019: '6-21',
         2020: '6-20'}
    d = a[year].split('-')
    r = {'name': 'Summer'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                The first day of summer is known as the summer solstice.
                 It marks the day when the sun appears highest in the sky.
                """
    r['alt_names'] = 'summer-solstice'
    r['link'] = 'http://en.wikipedia.org/wiki/Summer_solstice'
    r['link_title'] = 'Wikipedia'
    return r


# http://en.wikipedia.org/wiki/Tax_Day

def thanksgiving_day(year):
    # 4th Thursday of November
    d = get_nth_day_of_month(4, THU, NOV, year)
    r = {'name': 'Thanksgiving'}
    r['date'] = datetime(int(year), int(NOV), d, now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Thanksgiving Day is a national holiday celebrated primarily in the United States and Canada
                as a day of giving thanks for the blessing of the harvest and of the preceding year.
                It is celebrated on the fourth Thursday of November.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Thanksgiving'
    r['link_title'] = 'Wikipedia'
    return r

"""
def three_kings_day(year):
    r = {'name':'3 Kings Day'}
    r['date'] = datetime(int(year), int(JAN), int(6), now.hour, now.minute)
    r['desc'] = ''
    r['alt_names'] = ''
    r['link'] = ''
    r['link_title'] = ''
    return r
"""

def valentines_day(year):
    # Feb 14
    r = {'name': 'Valentine''s Day'}
    r['date'] = datetime(int(year), int(FEB), 14, now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                Saint Valentine's Day, also known as the Feast of Saint Valentine,
                is a holiday observed on February 14 each year.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Valentine%27s_Day'
    r['link_title'] = 'Wikipedia'
    return r


def veterans_day(year):
    # Nov 11
    r = {'name': 'Veterans''s Day'}
    r['date'] = datetime(int(year), int(NOV), 11, now.hour, now.minute)
    r['desc'] = """
                Veterans Day is an official United States holiday that honors people who have served in the U.S. Armed Forces.
                It is a federal holiday that is observed on November 11.
                """
    r['alt_names'] = ''
    r['link'] = 'http://en.wikipedia.org/wiki/Veterans_Day'
    r['link_title'] = 'Wikipedia'
    return r


def winter_day(year):
    a = {2012: '12-21', 2013: '12-21', 2014: '12-21', 2015: '12-22', 2016: '12-21', 2017: '12-21', 2018: '12-21',
         2019: '12-22', 2020: '12-21'}
    d = a[year].split('-')
    r = {'name': 'Winter'}
    r['date'] = datetime(int(year), int(d[0]), int(d[1]), now.hour, now.minute)
    r['priority'] = 100
    r['desc'] = """
                The first day of winter is known as the winter solstice.
                It is the shortest day and the longest night of the year.
                """
    r['alt_names'] = 'winter-solstice'
    r['link'] = 'http://en.wikipedia.org/wiki/Winter_solstice'
    r['link_title'] = 'Wikipedia'
    return r

    # washingtons bday feb 22