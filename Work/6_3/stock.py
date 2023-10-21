from structure import Structure
import inspect

class Stock(Structure):
    _fields = ()
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.set_fields()   