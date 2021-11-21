import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'car.xlsx'
data = pd.read_excel(path)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
D = data.iloc[:, 0]
D = list(D.unique())  # 车次好D02~D06
list1 = []      # 预定义每个车次的上车人数列表
for d in D:
    dt = data.loc[data['车次'] == d, ['上车人数']]
    s = dt.sum()
    list1.append(s['上车人数'])
plt.pie(list1, labels=D, autopct='%1.2f%%')     # 绘制饼图，百分比保留小数点后两位
plt.title('各车次上车人数商店图')
plt.show()
