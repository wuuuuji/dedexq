import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def drawbar(x, y, title, xlable, ylable):
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
    plt.title(title)  # 设置题目
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.xticks(rotation=45)
    plt.bar(x, y)
    plt.show()
    plt.savefig(title)


# 饼图显示2012欧洲杯黄牌数量
ero12 = pd.read_csv('Euro2012.csv')
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.pie(ero12['Yellow Cards'], labels=ero12['Team'])
plt.title('2012欧洲杯黄牌')
plt.show()
# 饼图显示2012欧洲杯进球超过4次的球队分布情况
index = ero12['Goals'] > 4
data5 = ero12.loc[index, :]
plt.pie(data5['Goals'], labels=data5['Team'])
plt.title('2012欧洲杯进球超过4次的球队分布情况')
plt.show()
# 柱状图显示各球队射正率
drawbar(ero12['Team'], ero12['Shooting Accuracy'], '各球队射正率', '球队', '分值')
