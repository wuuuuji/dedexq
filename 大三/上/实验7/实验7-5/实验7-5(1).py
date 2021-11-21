import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('D://learn/大三/上/实验7/实验7-5/data.xlsx')
plt.figure(1)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.plot(range(1, 11), df['猪肉价格'].values[:10], 'r*--')
plt.plot(range(1, 11), df['牛肉价格'].values[:10], 'b*--')
plt.xlabel('日期')
plt.ylabel('价格')
plt.title('猪肉和牛肉价格走势图')
plt.legend(['猪肉', '牛肉'])
plt.xticks(range(1, 11, 2), df['日期'].values[range(0, 10, 2)], rotation=90)
plt.show()

plt.figure(2)  # 2张子图
plt.subplot(2, 1, 1)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.plot(range(1, 16), df['猪肉价格'].values)
plt.xlabel('日期')
plt.ylabel('价格')
plt.title('猪肉价格走势图')
plt.xticks(range(1, 16, 2), df['日期'].values[range(0, 15, 2)], rotation=90)
plt.subplot(2, 1, 2)
plt.xlabel('日期')
plt.ylabel('价格')
plt.title('牛肉价格走势图')
plt.legend(['猪肉', '牛肉'])
plt.xticks(range(1, 16, 2), df['日期'].values[range(0, 15, 2)], rotation=90)
plt.tight_layout()
plt.show()

