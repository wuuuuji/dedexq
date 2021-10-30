import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = 'car.xlsx'
data = pd.read_excel(path)
tb = data.loc[data['车次'] == 'D02', ['日期', '上车人数']].sort_values('日期')
x = np.arange(1, len(tb.iloc[:,0])+1)
y1 = tb.iloc[:,1]
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.scatter(x, y1)  # 绘制散点图
plt.xlabel('日期')
plt.ylabel('上车日期')
plt.xticks([1, 5, 10, 15, 20, 24], tb['日期'].values[[0, 4, 9, 14, 19, 23]], rotation= 45)
plt.title('D02车次上车人数商店图')
plt.show()