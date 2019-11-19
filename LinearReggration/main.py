import pandas as pd
from os import path

from calculateVariable import *
from getData import *
from predictX import *
from RSquare import *
from graphEquation import *
from LR import *
import sys

def main():
    dataFileName = 'trainingData'
    trainingData = getData(dataFileName + '.xlsx')
    # calcalculate = calculateVariable(trainingData)
    # slope, Yintercept, yMean = calcalculate.getSlopeYintercept()
    # # createTrainingFile(trainingData,slope, Yintercept, yMean, dataFileName)
    # plot = graphEquation(trainingData, slope, Yintercept)
    # plot.drawGraph()
    # print(trainingData)
    # initializeEquation = predictX(slope, Yintercept)
    # initializeEquation.predictValue()
    #RSqaureValue = RSqaure(trainingData, slope, Yintercept, yMean)
    #print(RSqaureValue.calcuateR())
    x = LR(trainingData)
    x.trainModel()

if __name__ == '__main__':
    main()
