
from logcall import logged
from logcall import logformat

from validate import enforce
@logged
def add(x,y):
    'Adds two things'
    return x+y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def two(x,y):
    'Adds two things'
    return x+y




class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y