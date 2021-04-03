from statistics import variance
from math import sqrt

class TinyStatistician:
    
    @staticmethod
    def mean(array):
        if not array:
            return None
        sum = 0
        for i in array:
            sum += i
        return float(sum/len(array))

    @staticmethod
    def median(array):
        if not array:
            return None
        array.sort()
        size = len(array)
        if size % 2 != 0:
            return float(array[int(size/2)])
        else:
            ret = array[int((size/2)-1)] if array[int((size/2)-1)] < array[int((size/2))] else array[int((size/2))] 
            return float(ret)
    
    @staticmethod
    def quartile(array, percentile):
        if not array:
            return None
        array.sort()
        index = int(percentile / 100 * len(array))
        return float(array[index])
    
    @staticmethod
    def var(array):
        if not array:
            return None

        array.sort()
        mean = TinyStatistician.mean(array)

        deviations = [(item - mean) ** 2 for item in array]
        variance = sum(deviations) / len(array)

        return float(variance)
    
    @staticmethod
    def std(array):
        if not array:
            return None

        return float(sqrt(TinyStatistician.var(array)))






if __name__ == '__main__':
    array = [1, 42, 300, 10, 59]
    tstat = TinyStatistician()
    print("----------------------------")
    print("array:", array)
    print("----------------------------")
    print("mean:", tstat.mean(array))
    print("----------------------------")
    print("median:", tstat.median(array))
    print("----------------------------")
    print("quartile:", tstat.quartile(array, 25))
    print("quartile:", tstat.quartile(array, 75))
    print("----------------------------")
    print("var:", tstat.var(array))
    print("----------------------------")
    print("std:", tstat.std(array))
    print("----------------------------")
