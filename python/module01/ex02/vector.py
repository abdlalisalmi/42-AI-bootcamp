

class Vector:
    def __init__(self, arg) -> None:
        if isinstance(arg, int):
            self.values = [float(i) for i in range(0, arg)]
        elif isinstance(arg, list):
            self.values = arg
        elif isinstance(arg, tuple):
            self.values = [float(i) for i in range(arg[0], arg[1])]
        
        self.size = len(self.values)

    def __add__(self, scalar):
        if isinstance(scalar, Vector):
            result = []
            for s, o in zip(self.values, scalar.values):
                result.append(s + o)
            return Vector(result)
        else:
            return Vector([(value + scalar) for value in self.values])
    
    def __radd__(self, scalar):
        return self.__add__(scalar)

    def __sub__(self, scalar):
        if isinstance(scalar, Vector):
            result = []
            for s, o in zip(self.values, scalar.values):
                result.append(s - o)
            return Vector(result)
        else:
            return Vector([(value - scalar) for value in self.values])
    
    def __rsub__(self, scalar):
        if isinstance(scalar, Vector):
            result = []
            for s, o in zip(self.values, scalar.values):
                result.append(s - o)
            return Vector(result)
        else:
            return Vector([(scalar - value) for value in self.values])
    
    def __mul__(self, scalar):
        if isinstance(scalar, Vector):
            sum = 0
            for s, o in zip(self.values, scalar.values):
                sum += s * o
            return Vector([sum])
        else:
            return Vector([(value * scalar) for value in self.values])
        
    def __rmul__(self, scalar):
        return self.__truediv__(scalar)

    def __truediv__(self, scalar):
        return [(value / scalar) for value in self.values]
    
    def __rtruediv__(self, scalar):
        return [(scalar / value) for value in self.values]

    def __str__(self):
        return f"(Vector {self.values})"
    
    def __repr__(self):
        rep = f'Vector(Values: {self.values}, Size: {self.size})'
        return rep