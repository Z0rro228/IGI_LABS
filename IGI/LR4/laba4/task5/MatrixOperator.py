import numpy as np
import math


class MatrixOperator:
    '''Class for operating with random matrix.'''

    def __init__(self):
        self.__matrix = np.ndarray([0, 0])
    def generateMatrix(self, a: int, b: int):
        self.__matrix = np.random.rand(a, b)

    def __str__(self):
        for row in self.__matrix:
            print(row)
    def insertRowAfterMin(self):
        min_element = np.min(self.__matrix)
        min_index = np.where(self.__matrix == min_element)
        row, col = min_index[0][0], min_index[1][0]
        new_row = self.__matrix[0]
        a = np.insert(self.__matrix, row + 1, new_row, axis=0)
        return str(a)

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, input):
        self.__matrix = input
    def calculateMedianNumpy(self):
        return np.median(self.__matrix[0])
    def calculateMedian(self):
        sorted_row = np.sort(self.__matrix[0])
        n = len(sorted_row)
        if n % 2 == 0:
            return (sorted_row[n // 2 - 1] + sorted_row[n // 2]) / 2
        else:
            return sorted_row[n // 2]