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
from .help_method import get_weekday, read_day_file

TODAY = datetime.today()


class DailyAccountBook(BaseAccountBook):
    """Every day's expenditure's record."""
    def __init__(self,
                 year=TODAY.year,
                 month=TODAY.month,
                 day=TODAY.day):
        self.weekday = get_weekday()
        self.year = year
        self.month = month
        self.day = day
        self.records = []

    def read_data(self):
        """Read data from dataset json files"""
        return read_day_file(year=self.year,
                             month=self.month,
                             day=self.day)

    def save_data(self):
        """Save data into dataset json files"""
        raise NotImplementedError()

    def average_data(self):
        """Average data depending on type of the book"""
        raise NotImplementedError()

    def add_data(self):
        """Add a new data entry into the book"""
        raise NotImplementedError()

    def remove_data(self):
        """Remove data from the book"""
        raise NotImplementedError()

    def update_data(self):
        """Update data for any reasons"""
        raise NotImplementedError()

    def get_dict(self):
        """Get dict version for serialization"""
        raise NotImplementedError()
