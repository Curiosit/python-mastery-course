def typedproperty(expected_type):
    

    @special_property
    def value(self):
        return getattr(self, value.private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, value.private_name, val)
   
    return value

class special_property(property):
    def __set_name__(self, cls, name):
        self.public_name = name
        self.private_name = '_' + name
        super().__set_name__(cls, name)

def String():
    typedproperty(str)
def Integer():
    typedproperty(int)
def Float():
    typedproperty(float)


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
