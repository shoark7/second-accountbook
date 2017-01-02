"""
Define a daily account book.

It contains every entry of a day and be serialized to monthly account book.
Also, when it is about to be saved, it creates json file depending on a day.

Year
    Month
        day
        day
    Month
        day
        day
        day

Tree will be like this.
"""

from datetime import datetime
import json
import os
from .base_account_book import BaseAccountBook
from .help_method import get_weekday, get_path_day, get_path_month,\
        get_path_year, max_expenditure_length
from .record import Record

TODAY = datetime.today()


class DailyAccountBook(BaseAccountBook):
    """Every day's expenditure's record."""
    def __init__(self,
                 year=TODAY.year,
                 month=TODAY.month,
                 day=TODAY.day):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = get_weekday(self.year, self.month, self.day)
        self.data = dict()
        self.read_data()
        self.entry_count = len(self.data['records'])
        self.average_data()

    def __repr__(self):
        return '{}/{:02}/{:02} 지출내역'.format(
            self.year, self.month, self.day
        )

    def read_data(self):
        """Read data from dataset json files"""
        path = get_path_day(self.year, self.month, self.day)
        if os.path.exists(path):
            with open(path, 'r') as fp:
                self.data = json.load(fp,)
        else:
            self.get_dict()

    def save_data(self):
        """Save data into dataset json files"""
        path = get_path_day(self.year, self.month, self.day)
        path_month = get_path_month(self.year, self.month)
        path_year = get_path_year(self.year)

        if os.path.exists(path):
            with open(path, 'w') as fp:
                json.dump(self.data, fp,)
        else:
            if not os.path.exists(path_year):
                os.mkdir(path_year)
            if not os.path.exists(path_month):
                os.mkdir(path_month)
            with open(path, 'w') as fp:
                json.dump(self.data, fp, )

    def average_data(self):
        """Average data depending on type of the book"""

        if self.entry_count is 0:
            return
        self.average = 0
        self.total_sum = 0
        for record in self.data['records']:
            self.total_sum += record['money']
        self.average = self.total_sum // self.entry_count

    def add_data(self, money, reason=None):
        """Add a new data entry into the book"""
        new_record = Record(money, reason)
        self.entry_count += 1
        self.data['records'].append(new_record.get_dict())
        return None

    def remove_data(self):
        """Remove data from the book"""
        raise NotImplementedError()

    def update_data(self):
        """Update data for any reasons"""
        raise NotImplementedError()

    def get_dict(self):
        """Get dict version for first serialization"""
        self.data = dict()
        self.data['day'] = self.day
        self.data['records'] = []
        return None

    def statistic_day(self):

        """Shows daily expenditure overview.

        1. Simple statistics : sum and average
        2. print every single record.
        """

        if self.entry_count is 0:
            print('이 날은 지출내역이 없습니다.')
            return
        self.average_data()

        money_records = [record['money'] for record in self.data['records']]
        max_length_staticstics = max_expenditure_length([self.total_sum, self.average])
        max_length_entry = max_expenditure_length(money_records)
        max_length_line = len(str(self.entry_count))

        print()
        print('    {year}년 {month}월 {day}일 {weekday}요일 : 총 {count}건'.format(
                year=self.year,
                month=self.month,
                day=self.day,
                count=self.entry_count,
                weekday=self.weekday
        ))
        print('-' * 40)
        print('총 지출 : {:>{},}원'.format(self.total_sum, max_length_staticstics))
        print(' 평  균 : {:>{},}원'.format(self.average, max_length_staticstics))
        print('-' * 40)

        for i, record in enumerate(self.data['records']):
            print(' {line:^{line_length}} |  금 액  : {money:>{length},}원, 사유 : {reason}'.format(
                    line=i+1,
                    line_length=max_length_line,
                    money=record['money'],
                    length=max_length_entry,
                    reason=record['reason']
            ))
        print()
