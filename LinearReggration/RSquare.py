class RSqaure(object):
    global slope
    global Yintercept
    global xValues
    global yValues
    global yMean

    def __init__(self, trainingData, slope, Yintercept, yMean):
        self.slope = slope
        self.Yintercept = Yintercept
        self.yMean = yMean
        self.xValues = []
        self.yValues = []
        for numOfElements in range(0,len(trainingData)):
            self.xValues.append(trainingData[numOfElements][0])
            self.yValues.append(trainingData[numOfElements][1])

    def calcuateR(self):
        sumPredicted= 0
        sumActul = 0
        for y in self.yValues:
            sumActul = sumActul + ((y - self.yMean) * (y - self.yMean))
        for x in self.xValues:
            estimateValue = (self.slope * x) + self.Yintercept
            sumPredicted = sumPredicted + ((estimateValue - self.yMean) * (estimateValue - self.yMean))
        if (sumActul == 0):
            return 0
        else:
            return (sumPredicted/sumActul)
