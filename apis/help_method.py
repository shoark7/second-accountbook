"""
This file defines some helper methods for the project.
It's simple.

"""

from datetime import datetime
import json
import os

TODAY = datetime.today()
YEAR = TODAY.year
MONTH = TODAY.month
DAY = TODAY.day


def get_weekday():
    """Use datetime.today to get weekday in Korean."""
    WEEKDAY = ['월', '화', '수', '목', '금', '토', '일']

    return WEEKDAY[TODAY.weekday()]


def get_path_day(year, month, day):
    path = os.path.join('./dataset/{year}/{month:02}/{day:02}.json'.format(
    year=YEAR,
    month=MONTH,
    day=DAY))
    return path


def get_path_month(year, month):
    path = os.path.join('./dataset/{year}/{month:02}'.format(
                year=YEAR,
                month=MONTH,
        ))
    return path


def get_path_year(year):
    path = os.path.join('./dataset/{year}'.format(year=YEAR))
    return path

