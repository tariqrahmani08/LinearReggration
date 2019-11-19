import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#import dataset as a csv file from path
dataset = pd.read_csv('/Users/trahmani/Desktop/LinearReggration/listings.csv')
#features we want our model based on
x = dataset['reviews_per_month'].values.reshape(-1,1)
y = dataset['number_of_reviews'].values.reshape(-1,1)

#graph our features
dataset.plot(x='reviews_per_month', y='number_of_reviews', style='o')
plt.title('reviews_per_month vs number_of_reviews')
plt.xlabel('reviews_per_month')
plt.ylabel('number_of_reviews')
plt.show()

#reshape x and y as needed
X = np.array(x).reshape(-1,1)
Y = np.array(y).reshape(-1,1)

#split test and train set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

#graph our dataset with our LinearRegression model
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
