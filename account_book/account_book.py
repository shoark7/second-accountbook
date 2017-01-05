"""
Real account book using all other APIs.
Its contents would be like this.

1. Data input
    1) Once
    2) More than once
2. Data query
    1) Daily basis
    2) Monthly basis
    3) Yearly basis
    4) All(since first record to the last)
3. Data update
4. Data delete
5. Data print out
    1) local
    2) mail
    3) message
6. exit
"""

from datetime import datetime
import os
from ..apis.yearly_account_book import YearlyAccountBook
from ..apis.help_method import max_expenditure_length

TODAY = datetime.today()


class AccountBook:
    """
    Account book for execution.
    It loads all year, month and day account books
    and will be used with functions(apps) in main.py
    """

    def __init__(self):
        """
        Initialize account book with year, month, daily account books.
        """
        year_data_path = os.path.join('Accountbook_project/Accountbook/dataset')
        year_list = reversed(os.listdir(year_data_path))
        self.ledger = list()

        for year in year_list:
            year = int(year)
            new_year_book = YearlyAccountBook(year=year)
            self.ledger.append(new_year_book)

    def __getitem__(self, year):
        """
        Get year account book of that year.
        For example, book[3] gets expenditure data of March.
        book[7] gets expenditure data of July.
        """
        try:
            year_book = [book for book in self.ledger if book.year==year][0]
            return year_book
        except:
            print("해당 연도의 장부가 없습니다.")

    def __repr__(self):
        return "박성환의 {}년간 지출내역서".format(len(self.ledger))

    def average_data(self):
        """Average all entries and amount of expenditure."""
        self.total_entry = 0
        self.total_amount = 0

        for ledger in self.ledger:
            self.total_entry += ledger.entry_count
            self.total_amount += ledger.year_total

        if self.total_entry == 0:
            return
        self.total_average = self.total_amount // self.total_entry

    def statistic_all(self):
        """Average data and make it print out on stdout."""

        self.average_data()
        print()
        print('-' * 40)
        print("        지난 {}년간 총 사용보고서".format(len(self.ledger)))
        print('-' * 40)

        stats_length = max_expenditure_length([self.total_amount,
                                               self.total_entry,
                                               self.total_average])
        print("총 기록횟수 : {:{},}번".format(self.total_entry, stats_length))
        print("총 사용금액 : {:{},}원".format(self.total_amount, stats_length))
        print("\n총 평균금액 : {:{},}원".format(self.total_average, stats_length))
        print()
