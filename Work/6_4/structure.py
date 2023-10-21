# structure.py
import sys
import inspect

class Structure:
    _fields = ()

    def __repr__(self):
            return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
        
    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        code = 'def __init__(self, {0}):\n'.format(args)
        print(code)
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = { }
        print(code)
        exec(code, locs)
        cls.__init__ = locs['__init__']
