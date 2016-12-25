"""
This file defines some helper methods for the project.
It's simple.

"""

from datetime import datetime


def get_weekday():
    """Use datetime.today to get weekday in Korean."""
    WEEKDAY = ['월', '화', '수', '목', '금', '토', '일']
    today = datetime.today()

    return WEEKDAY[today.weekday()]

