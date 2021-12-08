import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as LR

# 1.数据获取
data = pd.read_excel('./data/发电场数据.xlsx')
# iloc[: , :]的作用，逗号前面的分号是限制行，后面一个是限制列，不填写就是读取全部。输出的类型是DataFrame
x = data.iloc[:, 0:4].values  # 读取0到3列的每一行，并转化为数组
y = data.iloc[:, 4].values

# 2.导入线性回归模块,简称LR
lr = LR()  # 创建线性回归模型类
lr.fit(x, y)  # 拟合
Slr = lr.score(x, y)  # 判定系数R^2
c_x = lr.coef_  # x对应的回归系数
c_b = lr.intercept_  # 回归系数常数数项

# 3.预测
x1 = np.array([28.4, 50.6, 1011.9, 80.54])
x1 = x1.reshape(1, 4)
R1 = lr.predict(x1)  # 采用自带函数预测
r1 = x1 * c_x
R2 = r1.sum() + c_b  # 计算其预测值
print('x回归系数为:', c_x)
print('回归系数常数项为:', c_b)
print('判定系数为:', Slr)
print('样本预测值为:', R1)
