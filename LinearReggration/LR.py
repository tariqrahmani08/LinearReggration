import numpy as np
from sklearn.linear_model import LinearRegression
from getData import *
import matplotlib.pyplot as plt

class LR(object):
    global trainingData
    global dataSize
    def __init__(self, trainingData):
        self.trainingData = trainingData
        self.dataSize = int(len(self.trainingData))
    def trainModel(self):
        xValue = []
        yValue = []
        for i in range(self.dataSize):
             xValue.append(self.trainingData[i][0])
             yValue.append(self.trainingData[i][1])


        X = np.array(xValue).reshape((-1, 1))
        Y = np.array(yValue)

        model = LinearRegression()
        model.fit(X, Y)

        plt.scatter(X, Y, color = "red")
        plt.plot(X, model.predict(X), color = "green")
        plt.title("Visualization of Data points")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.show()

        r_sq = model.score(X,Y)
        print('coefficient of determination:', r_sq)

        y_pred = model.predict(np.array(7.8).reshape((-1, 1)))
        print('predicted response:', y_pred, sep='\n')
