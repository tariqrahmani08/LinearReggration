import matplotlib.pyplot as plt
import math
class graphEquation(object):
    global trainingData
    global slope
    global Yintercept
    global dataSize
    def __init__(self, trainingData, slope, Yintercept):
        self.trainingData = trainingData
        self.slope = slope
        self.Yintercept = Yintercept
        self.dataSize = int(len(self.trainingData))

    def drawGraph(self):
        xValue = []
        yValue = []
        xPredict = []
        for i in range(self.dataSize):
             xValue.append(self.trainingData[i][0])
             yValue.append(self.trainingData[i][1])
        maxValueInList = int(math.ceil(max(xValue)) + self.dataSize)
        minValueInList = int(math.ceil(min(xValue)) - self.dataSize)

        xPredict = []
        yPredict = []
        for i in range(minValueInList, maxValueInList):
            xPredict.append(i)
            y = (self.slope * i) + self.Yintercept
            yPredict.append(y)
        plt.title('Visualization of Data points')
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.scatter(xValue, yValue,  color='black',marker='8')
        plt.plot(xPredict, yPredict, color='blue', linewidth=3)

        plt.show()
