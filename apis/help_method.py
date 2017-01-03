"""
This file defines some helper methods for the project.
It's simple.

"""

from datetime import datetime, date
import os

TODAY = datetime.today()
YEAR = TODAY.year
MONTH = TODAY.month
DAY = TODAY.day
ALL_MONTH_NAMES = [
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December',
]


def get_weekday(year=YEAR, month=MONTH, day=DAY):
    """Use datetime.today to get weekday in Korean."""
    WEEKDAY = ['월', '화', '수', '목', '금', '토', '일']
    DATE = date(year, month, day)

    return WEEKDAY[DATE.weekday()]


def get_month_name(month=MONTH):
    """Get month's full name in English"""

    return ALL_MONTH_NAMES[month-1]


def get_path_day(year, month, day):
    path = os.path.join('Accountbook/dataset/{year}/{month:02}/{day:02}.json'.format(
        year=year,
        month=month,
        day=day)
    )
    return path


def get_path_month(year=YEAR, month=MONTH):
    path = os.path.join('Accountbook/dataset/{year}/{month:02}'.format(
                year=year,
                month=month,
        ))
    return path


def get_path_year(year=YEAR):
    path = os.path.join('Accountbook/dataset/{year}'.format(year=year))
    return path


def max_expenditure_length(wanted_list):
    return len('{:,}'.format(max(wanted_list))) + 1
