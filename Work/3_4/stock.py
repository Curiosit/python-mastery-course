import csv
class Stock:
    __slots__ = ('name', 'shares', 'price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
    
    
    
    @property
    def shares(self,num):
        return self.shares
    @shares.setter
    def shares(self,value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected a {self._types[1].__name__}')
        if value < 0:
            raise ValueError('Shares must be >= 0')
        self._shares = value
    

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected a {self._types[2].__name__}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


    @property
    def cost(self):
        return self.shares * self.price
    def sell(self, num):
        self.shares -= num