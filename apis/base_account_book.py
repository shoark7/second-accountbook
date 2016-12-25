"""
This file provides basic interface for all account books.
I think subclasses of base account book would be
    1. daily basis
    2. monthly basis
    3. yearly basis
account books
"""


class BaseAccountBook(object):
    """Interface for all account book"""
    def __init__(self):
        """Initialize account book"""
        raise NotImplementedError()

    def read_data(self):
        """Read data from dataset json files"""
        raise NotImplementedError()

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
