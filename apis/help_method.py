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


def read_day_file(year=YEAR, month=MONTH, day=DAY):
    path = os.path.join('./dataset/{year}/{month:02}/{day:02}.json'.format(
        year=YEAR,
        month=MONTH,
        day=DAY))

    if os.path.exists(path):
        with open(path, 'r') as fp:
            result = json.load(fp)
        return result
    else:
        print('해당 날짜의 파일이 없습니다.')
        return
