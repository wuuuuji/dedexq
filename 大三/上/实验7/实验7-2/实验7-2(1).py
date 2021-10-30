import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # 季度标号
y = np.array([100, 104, 106, 95, 103, 105, 115, 110])   # 销售额
v = ['2018年一季度', '2018年二季度', '2018年三季度', '2018年四季度',
     '2019年一季度', '2019年二季度', '2019年三季度', '2019年四季度']
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.title('某产品2018-2019各季度销售额')
plt.plot(x, y)
plt.xlabel('季度')
plt.xticks(x, v, rotation=45) # v为与x对应的字符刻度，rotation为旋转角度
plt.ylabel('销售额(万元)')
plt.show()