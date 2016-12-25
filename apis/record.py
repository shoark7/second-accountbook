"""
record.py defines each expenditure entry.
It will be serialized into Account book's json file.
"""

from datetime import datetime


TODAY = datetime.today()


class Record:
    """Every expenditure's record."""
    def __init__(self, money, reason='미상'):
        self.money = int(money)
        self.reason = reason

    def get_dict(self):
        """Get dict for serialization."""
        result = {}
        result['money'] = self.money
        result['reason'] = self.reason
        result['hour'] = TODAY.hour
        result['minute'] = TODAY.minute
        return result

    @property
    def prettify_time(self):
        return '{}'.format(TODAY.strftime(format='%H:%M'))

    @property
    def prettify_money(self):
        return '{:,}원'.format(self.money)
