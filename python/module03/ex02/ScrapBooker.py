import os
import numpy as np

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-4] + 'ex01')
import ImageProcessor as ip



class ScrapBooker:
    

    @staticmethod
    def crop(array, dimensions, position=(0,0)):
        height, width = len(array), len(array[0])
        new_height, new_width = dimensions
        y, x = position

        if dimensions <= tuple([height, width]):
            return array[y:y+new_height, x:x+new_width]
        else:
            raise ValueError("Dimentions is larger than the current image size!")
    

    @staticmethod
    def thin(array, n, axis):
        result = []
        if axis == 0:
            for arr in array:
                tmp = list(arr)
                for i in range(n-1,len(tmp) - 1, n-1):
                    if i <= len(tmp) - 1:
                        del tmp[i]
                result.append(tmp)
        elif axis == 1:
            result = list(array)
            for i in range(n-1,len(result) - 1, n-1):
                if i <= len(result) - 1:
                        del result[i] 
        return np.array(result)



    @staticmethod
    def juxtapose(array, n, axis):
        pass


    @staticmethod
    def mosaic(array, dimensions):
        pass






if __name__ == '__main__':

    sb = ScrapBooker()

    """Test Crop"""
    # imp = ip.ImageProcessor()
    # arr = imp.load("../resources/42AI.png")
    # imp.display(arr)

    # arr = sb.crop(arr, (100, 100))
    # imp.display(arr)

    """Test Thin"""
    array = np.array([
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L'],
        ['A','B','C','D','E','F','G','H','I','J','Q','L']
    ])
    array2 = np.array([
        ['A','A','A','A','A','A','A','A','A','A','A','A'],
        ['B','B','B','B','B','B','B','B','B','B','B','B'],
        ['C','C','C','C','C','C','C','C','C','C','C','C'],
        ['D','D','D','D','D','D','D','D','D','D','D','D'],
        ['E','E','E','E','E','E','E','E','E','E','E','E'],
        ['F','F','F','F','F','F','F','F','F','F','F','F'],
        ['G','G','G','G','G','G','G','G','G','G','G','G'],
        ['H','H','H','H','H','H','H','H','H','H','H','H'],
        ['I','I','I','I','I','I','I','I','I','I','I','I'],
        ['J','J','J','J','J','J','J','J','J','J','J','J'],
        ['K','K','K','K','K','K','K','K','K','K','K','K'],
        ['L','L','L','L','L','L','L','L','L','L','L','L'],
    ])

    # print(sb.thin(array, 3, 0))
    # print(sb.thin(array2, 4, 1))
