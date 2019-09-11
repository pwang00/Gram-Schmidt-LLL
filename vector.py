from fractions import Fraction
from math import sqrt

class vector(object):

    int_array = []
    magnitude = 0
    
    def __init__(self, v):
        if type(v) in [list, tuple]:
            self.int_array = [int(i) if int(i) == i else i for i in v]
        elif type(v) == vector:
            self.int_array = v.get_values()
        self.magnitude = sqrt(sum([v_i ** 2 for v_i in self.int_array]))
        
    def get_values(self):
        return self.int_array

    def __mul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])

    def __rmul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])
    
    def __iter__(self):
        return iter(self.int_array)
    
    def __iadd__(self, v):
        self.int_array = [v.get_values()[i]+self.int_array[i] for i in range(len(self.int_array))]
        return vector(self.int_array)
    
    def __add__(self, v):
        return vector([v.get_values()[i]+self.int_array[i] for i in range(len(self.int_array))])

    def __sub__(self, v):
        return vector([self.int_array[i]-v.get_values()[i] for i in range(len(self.int_array))])

    def __isub__(self, v):
        self.int_array = [self.int_array[i] - v.get_values()[i] for i in range(len(self.int_array))]
        return vector(self.int_array)
    
    def dot_product(self, v):
        assert len(v.get_values()) == len(self.int_array)
        return sum([v.get_values()[i]*self.int_array[i] for i in range(len(self.int_array))])
        
    def normalize(self):
        self.int_array = [v / self.magnitude for v in self.int_array]
        return vector(self.int_array)

    def fraction_form(self, denom_limit):
        return tuple([Fraction(i).limit_denominator(denom_limit) if int(i) != i else i for i in self.int_array])

    def __repr__(self):
        return repr(tuple(self.int_array))
    
if __name__ == "__main__":
    v = vector([1, 2, 3, 4])
    print(v.dot_product(v))
    print(v+v)
    print(2*v)
