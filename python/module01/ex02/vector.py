



class Vector:
    def __init__(self, arg) -> None:
        if isinstance(arg, int):
            self.values = [float(i) for i in range(0, arg)]
        elif isinstance(arg, list):
            self.values = arg
        elif isinstance(arg, tuple):
            self.values = self.values = [float(i) for i in range(arg[0], arg[1])]
        
        self.size = len(self.values)

    def __add__(self, scalar):
        if isinstance(scalar, Vector):
            pass
        else:
            return Vector([(value + scalar) for value in self.values])
    
    def __radd__(self, scalar):
        return self.__add__(scalar)

    def __sub__(self, scalar):
        return Vector([(value - scalar) for value in self.values])
    
    def __rsub__(self, scalar):
        return Vector([(scalar - value) for value in self.values])
    
    def __truediv__(self, scalar):
        return Vector([(value * scalar) for value in self.values])
    
    def __rtruediv__(self, scalar):
        return self.__truediv__(scalar)

    def __str__(self):
        return f"(Vector {self.values})"
    
    def __repr__(self):
        rep = f'Vector(Values: {self.values}, Size: {self.size})'
        return rep



v = Vector([0.0, 1.0, 2.0, 3.0])
# print(repr(v))
# print(v.values, v.size)

v2 = 2 - v
print(v2)