def typedproperty(name, expected_type):
    private_name = '_' + name

    @special_property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value

class special_property(property):
    def __set_name__(self, cls, name):
        self.public_name = name
        self.private_name = '_' + name
        super().__set_name__(cls, name)

def String(value):
    typedproperty(value, str)
def Integer(value):
    typedproperty(value, int)
def Float(value):
    typedproperty(value, float)


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
