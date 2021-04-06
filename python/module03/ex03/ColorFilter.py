import os
import numpy as np

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-4] + 'ex01')
import ImageProcessor as ip


class ColorFilter:

    @staticmethod
    def invert(array):
        return 255 - array[:, :, :3]
        # result = []
        # for arr in array:
        #     a = []
        #     for vector in arr:
        #         v = []
        #         for index in vector:
        #             v.append(255 - index if index < 255 else 255)
        #         a.append(v)
        #     result.append(a)
        # return np.array(result)


    @staticmethod
    def to_blue(array):
        pass


    @staticmethod
    def to_green(array):
        pass


    @staticmethod
    def to_red(array):
        pass


    @staticmethod
    def to_celluloid(array):
        pass


if __name__ == '__main__':
    image = ip.ImageProcessor()
    array = image.load(os.path.dirname(os.path.abspath(__file__))[:-4] + 'assets/img.png')
    # image.display(array)

    cf = ColorFilter()
    image.display(cf.invert(array))
    cf.invert(array)