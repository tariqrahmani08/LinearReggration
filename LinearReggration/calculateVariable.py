import pandas as pd

class calculateVariable():
    global trainingData
    global dataSize

    def __init__(self, trainingData):
        self.trainingData = trainingData
        self.dataSize = int(len(self.trainingData))

    def getSlopeYintercept(self):
        xMean, yMean = self.getXYmean()
        slope = self.getSlope(xMean, yMean)
        Yintercept = self.getYintercept(xMean, yMean, slope)
        return slope, Yintercept, yMean

    def getSlope(self, xMean, yMean):
        top = 0
        bottom = 0
        for x in range(self.dataSize):
            top = (self.trainingData[x][0] - xMean) * (self.trainingData[x][1] - yMean)
            bottom = (self.trainingData[x][0] - xMean) * (self.trainingData[x][0] - xMean)
        slope = top / bottom
        return slope

    def getXYmean(self):
        xMean = 0
        yMean = 0
        for x in range(self.dataSize):
            xMean = xMean + self.trainingData[x][0]
            yMean = yMean + self.trainingData[x][1]
        xMean = xMean / self.dataSize
        yMean = yMean / self.dataSize
        return xMean, yMean

    def getYintercept(self, xMean, yMean, slope):
        return yMean - (xMean * slope)
