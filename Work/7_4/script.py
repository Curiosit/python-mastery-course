#a)

def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

def cost(self):
        return self.shares*self.price

def sell(self,nshares):
        self.shares -= nshares

methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell } 

Stock = type('Stock',(object,),methods)


#b)

from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())