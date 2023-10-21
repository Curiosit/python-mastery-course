def add(x,y):
       'Adds two things'
       return x+y


import inspect
sig = inspect.signature(add)
sig

sig.parameters

tuple(sig.parameters)