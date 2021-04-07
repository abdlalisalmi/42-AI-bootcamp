import os
import numpy as np

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:-4] + 'ex01')
import ImageProcessor as ip


class ColorFilter:

    @staticmethod
    def invert(array):
        # remove the alpha from the image array
        array = array[:, :, :3]

        # get all index < 255
        index = array[:,:,2] < 255

        # to make an index inverted we use this formula (255 - array[index])
        array[index] = 255 - array[index]
        return array


    @staticmethod
    def to_blue(array):
        # get all index < 255
        index = array[:,:,2] < 255

        # change the index 2 (rgb: r=0, g=1, b=2) to 255
        array[index, 2] = 255
        return array
        

    @staticmethod
    def to_green(array):
        # get all index < 255
        index = array[:,:,2] < 255

        # change the index 1 (rgb: r=0, g=1, b=2) to 255
        array[index, 1] = 180
        return array


    @staticmethod
    def to_red(array):
        # get all index < 255
        index = array[:,:,2] <= 255

        # change the index 0 (rgb: r=0, g=1, b=2) to 255
        array[index, 0] = 255
        return array


    @staticmethod
    def to_celluloid(array):
        pass


    @staticmethod
    def to_grayscale(array, filter):
        pass


if __name__ == '__main__':
    image = ip.ImageProcessor()
    array = image.load(os.path.dirname(os.path.abspath(__file__))[:-4] + 'assets/img.png')
    # image.display(array)

    cf = ColorFilter()
    image.display(cf.invert(array))
    # image.display(cf.to_blue(array))
    # image.display(cf.to_green(array))
    # image.display(cf.to_red(array))
    