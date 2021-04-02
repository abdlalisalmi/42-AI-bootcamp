

class Matrix:
    def __init__(self, data, shape=None):
        self.data = []

        if data and shape:
            self.data = data
            self.shape = shape

        elif isinstance(data, list):
            self.data = data
            self.shape = (len(self.data), len(self.data[0]))

        elif isinstance(data, tuple):
            self.data = self.create_empty_matrix(data)
            self.shape = data
        

    def __add__(self, matrix):
        if self.shape != matrix.shape:
            raise ValueError("The two matrices is not in the same dimension!")
        
        result = self.create_empty_matrix(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self.data[i][j] + matrix.data[i][j]
        return result

    def __radd__(self, matrix):
        return self.__add__(matrix)
    
    def __sub__(self, matrix):
        if self.shape != matrix.shape:
            raise ValueError("The two matrices is not in the same dimension!")
        
        result = self.create_empty_matrix(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self.data[i][j] - matrix.data[i][j]
        return result
    
    def __rsub__(self, matrix):
        return self.__sub__(matrix)

    def __mul__(self, arg):
        if isinstance(arg, list):
            data = []
            for matrix in self.data:
                result = []
                for index, v in zip(matrix, arg):
                    result.append(index * v)
                sum = 0
                for i in result:
                    sum += i
                data.append(sum)
            return data

        elif isinstance(arg, (int, float)):
            result = self.create_empty_matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = self.data[i][j] * arg
            return result
        elif isinstance(arg, Matrix):
            if self.shape != arg.shape:
                raise ValueError("The two matrices is not in the same dimension!")
            
            result = self.create_empty_matrix(self.shape)
            for i in range(arg.shape[0]):
                for j in range(arg.shape[1]):
                    for k in range(arg.shape[0]):
                        # resulted matrix
                        result[i][j] += self.data[i][k] * arg.data[k][j]
            return result

        else:
            raise TypeError(f"Unsupported operand for *: 'Matrix' and '{type(arg)}'")
    
    def __rmul__(self, arg):
        return self.__mul__(arg)

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            result = self.create_empty_matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = self.data[i][j] / scalar
            return result

        else:
            raise TypeError(f"Unsupported operand for *: 'Matrix' and '{type(scalar)}'")
    
    def __rtruediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            result = self.create_empty_matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result[i][j] = scalar / self.data[i][j]
            return result

        else:
            raise TypeError(f"Unsupported operand for *: 'Matrix' and '{type(scalar)}'")

    def __str__(self) -> str:
        return f"Matrix {self.data}"

    def __repr__(self) -> str:
        return f"Matrix (Data:{self.data}, Shape: {self.shape})"

    def create_empty_matrix(self, shape):
        matrix = []
        for i in range(shape[0]):
                matrix.append([float(0) for j in range(shape[1])])
        return matrix

