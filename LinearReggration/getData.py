import os
import xlrd
import pandas as pd
import xlsxwriter
from xlutils.copy import copy as xl_copy

global fileName
class getData(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def __new__(cls, fileName):
        filePath = str(os.getcwd())
        fileWithDate = xlrd.open_workbook(filePath +'/'+ fileName)
        fileWithDate = fileWithDate.sheet_by_index(0)
        trainingData = [[fileWithDate.cell_value(row, col)
            for col in range(fileWithDate.ncols)]
                for row in range(1, int(fileWithDate.nrows))]
        return trainingData
