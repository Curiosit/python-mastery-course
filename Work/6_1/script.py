from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year', 'month', 'day')

s = Stock('GOOG',100,490.1)
s.shares = 50
s.share = 50