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
from .help_method import get_path_month, get_month_name, max_expenditure_length

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
        self.average_data()

    def __repr__(self):
        """Decide form of object when entered."""
        return '{}년 {}월 지출내역'.format(self.year, self.month)

    def __getitem__(self, day):
        """By indexing object, you get daily data of the index number.

        Like object[30] means 'Get 30th data of that month.'
        If data of that day doesn't exists, error message is printed out."""

        try:
            return [record for record in self.data if record.day == day][0]
        except:
            return "{}/{:02}/{:02}의 기록이 존재하지 않습니다.".format(
                self.year, self.month, day,
            )

    def read_data(self):
        """Read data from dataset json files"""
        self.day_count = 0
        path = get_path_month(self.year, self.month)
        if os.path.exists(path):
            file_name_list = reversed(os.listdir(path))

            for file_name in file_name_list:
                day_number, ext = os.path.splitext(file_name)
                day_number = int(day_number)
                day_book = DailyAccountBook(self.year, self.month, day_number)
                self.data.append(day_book)
                self.day_count += 1
        else:
            print('해당 연도, 월의 데이터가 없습니다.')
            raise ValueError('Not available data')

    def average_data(self):
        """Get month average, total spent amount, total entry count."""
        self.month_total, self.month_average = 0, 0
        self.entry_count = 0

        if self.day_count == 0:
            return

        for day_data in self.data:
            day_total, day_average = day_data.total_sum, day_data.average
            self.entry_count += day_total // day_average
            self.month_total += day_total
        self.month_average = self.month_total // self.day_count

    def statistic_month(self):
        """Get total amount of expenditure and average of daily amount."""

        max_length = max_expenditure_length([self.month_total, self.month_average])
        if self.year == TODAY.year and self.month == TODAY.month:
            print('\n       {year}년 {month}월 {day}일 현재까지'.format(
                year=self.year,
                month=self.month,
                day=TODAY.day
            ))
            print('-' * 40)
            print('총 {}일 {}회\n'.format(self.day_count, self.entry_count))
            print('월 누적 지출금액 : {total:{length},}원\n월 누적 평균금액 : {average:{length},}원'.format(
                total=self.month_total,
                average=self.month_average,
                length=max_length)
            )
            print('-' * 40, '\n')

        else:
            print('\n           {year}년 {month}월 지출내역'.format(
                year=self.year,
                month=self.month,
                day=TODAY.day
            ))
            print('-' * 40)
            print('  총 {}일 {}회\n'.format(self.day_count, self.entry_count))
            print('-' * 40, '\n')
            print('  월 누적 지출금액 : {total:{length},}원\n월 누적 평균금액 : {average:{length},}원'.format(
                total=self.month_total,
                average=self.month_average,
                length=max_length)
            )

    def statistic_day_all(self):
        """Print all days' statistic data."""
        for data in self.data:
            data.statistic_day()
            print()
