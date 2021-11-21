import matplotlib.pyplot as plt

from sklearn import linear_model
x = [[1.], [2.], [3.], [4.], [5.]]
y = [[1.], [3.], [2.], [3.], [5.]]

model = linear_model.LinearRegression()
model.fit(x, y)
y_hat1 = model.predict(x)
plt.scatter(x, y)
plt.plot(x, y_hat1)
plt.axis([0, 6, 0, 6])
plt.show()
print('a='+model.coef_)
print('b='+model.intercept_)
