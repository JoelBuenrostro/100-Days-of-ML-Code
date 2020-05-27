# Simple linear regression

# Linear regression is a statistical machine learning method you
# can use to quantify, and make predictions based on relationships
# between numerical variables.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from pylab import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = 8, 6

rooms = 2 * np.random.rand(100, 1) + 3

price = 265 + 6*rooms +abs(np.random.rand(100, 1))

# Uncomment if you want the plot
# plt.plot(rooms, price, 'r^')
# plt.xlabel('# of rooms, 2019 average')
# plt.ylabel('2019 average house')
# plt.show()

x = rooms
y = price

model = LinearRegression()
model.fit(x, y)

print(model.intercept_, model.coef_)
print(model.score(x, y))