"""
Define a monthly account book.

It contains year and month info, and
daily account book information of that month.
Supports month dedicated statistical method, I hpe.
"""


from datetime import datetime
import os
from .base_account_book import BaseAccountBook
from .daily_account_book import DailyAccountBook
from .help_method import get_path_month, get_month_name

TODAY = datetime.today()


class MonthlyAccountBook(BaseAccountBook):
    """A month's expenditure record saved."""
    def __init__(self,
                 year=TODAY.year,
                 month=TODAY.month,
                 ):
        self.year = year
        self.month = month
        self.month_name = get_month_name(self.month)
        self.data = list()
        self.read_data()

    def __repr__(self):
        return '{}년 {}월 지출자료'.format(self.year, self.month)

    def read_data(self):
        """Read data from dataset json files"""
        self.count = 0
        path = get_path_month(self.year, self.month)
        if os.path.exists(path):
            file_name_list = os.listdir(path)

            for file_name in file_name_list:
                day_number, ext = os.path.splitext(file_name)
                day_number = int(day_number)
                day_book = DailyAccountBook(self.year, self.month, day_number)
                self.data.append(day_book)
                self.count += 1
        else:
            self.get_dict()

    def average_data(self):
        raise NotImplementedError()

    def get_dict(self):
        """Get dict version for first serialization"""
        self.data['month'] = self.month
