import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])
model = LinearRegression()
print(x)
print(y)

model.fit(x, y)

r2 = model.score(x, y)
print('coefficient of determination:', r2)
print('intercept:', model.coef_)

y_predict = model.intercept_ + model.coef_ * x
print('predicted response:', y_predict, sep='\n')