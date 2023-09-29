import csv
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, num):
        self.shares -= num

def read_portfolio(filename):

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        records = []
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            records.append(record)
    return records

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

# portfolio = read_portfolio('portfolio.csv')