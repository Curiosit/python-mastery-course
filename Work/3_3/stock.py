import csv
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
    def cost(self):
        return self.shares * self.price
    def sell(self, num):
        self.shares -= num

""" def read_portfolio(filename, cls):

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        records = []
        for row in rows:
            record = cls.from_row(row)
            
            records.append(record)
    return records """

""" def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
 """
# portfolio = read_portfolio('portfolio.csv')