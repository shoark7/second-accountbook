"""
Define a yearly account book.

It contains a whole year data, and
monthly account book information of that year.
Supports year dedicated statistical method, I hpe.
"""


from datetime import datetime
import os
from .base_account_book import BaseAccountBook
from .help_method import get_path_year, max_expenditure_length, ALL_MONTH_NAMES
from .monthly_account_book import MonthlyAccountBook

TODAY = datetime.today()


class YearlyAccountBook(BaseAccountBook):
    """A year's expenditure records are all saved."""
    def __init__(self, year=TODAY.year,):
        self.year = year
        self.data = list()
        self.entry_count = 0
        self.day_count = 0
        self.month_count = 0
        self.read_data()
        self.average_data()

    def __repr__(self):
        """Decide form of object when entered."""
        return '{}년 지출내역'.format(self.year)

    def __getitem__(self, month):
        """By indexing object, you get month data of the index number.

        Like object[10] means 'Get October's data of that year.'
        If data of that month doesn't exists, error message is printed out."""

        try:
            return [month_data for month_data in self.data if month_data.month == month][0]
        except:
            return "{}년 {:02}월의 기록이 존재하지 않습니다.".format(
                self.year, month
            )

    def read_data(self):
        """Read data from dataset json files"""
        self.month_count = 0
        path = get_path_year(self.year,)
        if os.path.exists(path):
            file_name_list = os.listdir(path)

            for file_name in file_name_list:
                file_name = int(file_name)
                month_book = MonthlyAccountBook(self.year, file_name)
                self.data.append(month_book)
                self.month_count += 1
        else:
            print('해당 연도의 데이터가 없습니다.')
            raise ValueError('No available data')

    def average_data(self):
        """Get month average, total spent amount, total entry count."""
        self.year_total, self.year_average = 0, 0

        if self.month_count == 0:
            return

        for month_data in self.data:
            self.entry_count += month_data.entry_count
            self.day_count += month_data.day_count
            self.year_total += month_data.month_total
        self.year_average = self.year_total // self.day_count

    def statistic_year(self):
        """Simply shows the year's data."""
        max_length = max_expenditure_length([self.year_average, self.year_total])
        max_length_legend = 10

        print('\n')
        print('-' * 60)
        print('                         {year}년{end} 보고서                '.format(
            year=self.year,
            end=' 결산' if self.year != TODAY.year else ''
        ))
        print('-' * 60)
        print('| {day:{max_length_legend}} : {day_count:>{max_length_count},}일'.format(
            day='기록 일수',
            max_length_legend=max_length_legend,
            day_count=self.day_count,
            max_length_count=max_length
            ),
            end=' | '
        )
        print('{entry:{max_length_legend}} : {entry_count:>{max_length_count},}번'.format(
            entry='입력 횟수',
            max_length_legend=max_length_legend,
            entry_count=self.entry_count,
            max_length_count=max_length
            ),
        )
        print('| {total:{max_length_legend}} : {total_amount:>{max_length},}원'.format(
            total='지출 금액',
            max_length_legend=max_length_legend,
            total_amount=self.year_total,
            max_length=max_length
            ),
            end=' | '
        )
        print('{average:{max_length_legend}} : {average_amount:>{max_length},}원'.format(
            average='평균 금액',
            max_length_legend=max_length_legend,
            average_amount=self.year_average,
            max_length=max_length
            ),
        )
        print('-' * 60)

    def statistic_month(self):
        """Get this year's statistics of all months."""
        max_length_legend = 10
        max_length = max_expenditure_length([self.year_average, self.year_total])

        month_string = '|'
        month_string += '{:^{}} |'.format('금액 종류', max_length_legend)

        for i in range(12):
            month_string += '{i:^{length}} |'.format(i=ALL_MONTH_NAMES[i][:3],
                                                        length=max_length)
        delimeter_length = len(month_string) + 5

        total_string = '|'
        total_string += '{:^{}} |'.format('지출 금액', max_length_legend)
        average_string = '|'
        average_string += '{:^{}} |'.format('평균 금액', max_length_legend)

        for i in range(1, 13):
            try:
                book = self[i]
                total_string += '{:{},} |'.format(book.month_total, max_length)
                average_string += '{:{},} |'.format(book.month_average, max_length)
            except:
                total_string += '{:^{}} |'.format('.', max_length)
                average_string += '{:^{}} |'.format('.', max_length)

        print('\n')
        print('-' * delimeter_length)
        year_string = '{}년 월별 지출 금액'.format(self.year)
        print('| {:^{}}|'.format(year_string, delimeter_length - 11))
        print('-' * delimeter_length)
        print(month_string)
        print('-' * delimeter_length)
        print(total_string)
        print('-' * delimeter_length)
        print(average_string)
        print('-' * delimeter_length)

    def statistic_month_all(self):
        """Print all days' statistic data."""
        for data in self.data:
            data.simple_statistic()
            print()
