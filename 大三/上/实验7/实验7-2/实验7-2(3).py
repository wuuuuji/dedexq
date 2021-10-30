import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = 'car.xlsx'
data = pd.read_excel(path)
tb = data.loc[data['车次'] == 'D02', ['日期', '上车人数']]
tb = tb.sort_values('日期')
tb1 = data.loc[data['车次'] == 'D03', ['日期', '上车人数']]
tb1 = tb1.sort_values('日期')
x = np.arange(1, len(tb.iloc[:,0])+1)
y1 = tb.iloc[:,1]
y2 = tb1.iloc[:,1]
plt.figure(1)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.plot(x, y1, 'r*--')     # 红色的*号连续图,绘制D02
plt.plot(x, y2, 'b*--')     # 蓝色的*号连续图,绘制D03
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.title('上车人数走势图')
plt.legend(['D02','D03'])
plt.xticks([1, 5, 10, 15, 20, 24], tb['日期'].values[[0, 4, 9, 14, 19, 23]], rotation= 45)
plt.show()