import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model

def runnplt(size=None):
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.figure(figsize=size)
    plt.title('披萨价格与直径数据')
    plt.xlabel('直径(英寸)')
    plt.ylabel('价格(美元)')
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt

plt = runnplt()
X = [[6], [8], [10], [14], [18]]      # 直径(英寸)
y = [[7], [9], [13], [17.5], [18]]    # 价格(美元)
plt.plot(X, y, 'k.')
plt.show()

model = linear_model.LinearRegression()
model.fit(X, y)
print('b=', model.intercept_)       # 截距
print('a=', model.coef_)        # 线性模型的系列
a = model.predict([[12]])

print('预测一张12英寸匹萨价格:{:.2f}'.format(model.predict([[12]])[0][0]))
