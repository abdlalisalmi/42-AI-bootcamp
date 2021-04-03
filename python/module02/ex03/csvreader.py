import os



class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.fd = None
        self.data = ""
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.sep = sep
        self.corrupted = False
        
    
    def getdata(self):
        if self.corrupted:
            return "The file is corrupted!"
        data = self.data.split('\n')[1:]
        if self.header:
            data = data[1:]
        if self.skip_top > 0:
            data = data[self.skip_top-1:]
        if self.skip_bottom > 0:
            data = data[:(len(data) - self.skip_bottom)]
        result = []
        for line in data:
            result.append(line.split(self.sep))
        return result
    
    def getheader(self):
        if self.corrupted:
            return "The file is corrupted!"
        if self.header:
            return self.data.split('\n')[0].split(self.sep)


    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r')
            self.data = self.fd.read()
            if self.is_corrupted():
                self.corrupted = True
            return self
        except FileNotFoundError:
            return None

    def __exit__(self, type, value, tb):
        if self.fd:
            self.fd.close()
    
    def is_corrupted(self):
        data = self.data.split('\n')
        first_line = data[0]
        for line in data:
            if len(first_line.split(self.sep)) != len(line.split(self.sep)):
                return True
        return False






if __name__ == "__main__":
    good_file = os.path.dirname(os.path.realpath(__file__)) + '/good.csv'
    with CsvReader(good_file, header=True, skip_top=10, skip_bottom=10) as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)
    
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")