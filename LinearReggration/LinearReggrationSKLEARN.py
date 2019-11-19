import numpy as np
from sklearn.linear_model import LinearRegression
from getData import *
import matplotlib.pyplot as plt

class LinearRegressionSKLEARN(object):
    global = trainingData
    def __init__(self, trainingData):
        self.trainingData = trainingData

    def trainModel(self):
        xValue = []
        yValue = []
        for i in range(self.dataSize):
             xValue.append(self.trainingData[i][0])
             yValue.append(self.trainingData[i][1])

        X = np.array(X).reshape((-1, 1))
        Y = np.array(Y)

        model = LinearRegression()
        model.fit(X, Y)

        plt.scatter(xValue, yValue, color = "red")
        plt.plot(xValue, lr.predict(xValue), color = "green")
        plt.title("Visualization of Data points")
        plt.xlabel("X Values")
        plt.ylabel("Y Values")
        plt.show()

        r_sq = model.score(X,Y)
        print('coefficient of determination:', r_sq)

        y_pred = model.predict(np.array(7.8).reshape((-1, 1)))
        print('predicted response:', y_pred, sep='\n')
