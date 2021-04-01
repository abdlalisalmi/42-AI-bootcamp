


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
            for i in range(data[0]):
                self.data.append([float(0) for j in range(data[1])])
            self.shape = data
        


m = Matrix((3, 2))
print(m.data, m.shape)