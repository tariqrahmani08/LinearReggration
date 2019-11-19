import os
import xlrd
import pandas as pd

global slope
global Yintercept

class predictX(object):

    def __init__(self,slope, Yintercept):
        self.slope = slope
        self.Yintercept = Yintercept

    def predictValue(self):
        while(True):
            xValue = input("\nWhat X-Value do you wish for this model to predict?: ")
            if xValue == "":
                print("Thank you")
                break
            try:
                print((self.slope*float(xValue)) + self.Yintercept)
            except ValueError:
                print("\nPlease eneter a number.")
