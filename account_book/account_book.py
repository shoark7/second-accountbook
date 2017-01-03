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
        year_data_path = os.path.join('Accountbook/dataset')
        year_list = reversed(os.listdir(year_data_path))
        self.ledger = list()

        for year in year_list:
            year = int(year)
            new_year_book = YearlyAccountBook(year=year)
            self.ledger.append(new_year_book)

    def __getitem__(self, year):
        """
        Get yearly account book of that year.
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

    def statistic_all(self):
        pass
