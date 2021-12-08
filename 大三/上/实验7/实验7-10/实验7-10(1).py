import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']        # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
data = pd.read_csv('./data/train.csv')
data.head(10)
data.describe()
print("缺少数据:\n", data.isnull().sum())

fig = plt.figure(figsize=(10, 10))      # 设置一个画布尺寸为10*10
fig.set(alpha=0.5)      # 设定图表颜色alpha参数

# 统计生还者与遇难者的比例
plt.subplot2grid((2, 3), (0, 0))        # 画第一幅图
# 在一张大图里,(2, 3)表示图像分布为2行3列。(0, 0)指的是第一行第一个
data.Survived.value_counts().plot(kind='bar')       # bar表示画的条形图
plt.title("获救情况（1为获救）")         # 第一幅小图的标题
plt.ylabel("人数")        # y轴

plt.subplot2grid((2, 3), (0, 1))        # 画第二幅图
data.Pclass.value_counts().plot(kind="bar")          # bar表示画的条形图
plt.title("乘客等级分布")         # 第二幅小图的标题
plt.ylabel("人数")        # y轴

plt.subplot2grid((2, 3), (0, 2))        # 画第三幅图
plt.scatter(data.Survived, data.Age)
plt.grid(b=True, which='major', axis='y')
plt.title("按年龄看获救分布（1为获救）")         # 第三幅小图的标题
plt.ylabel("年龄")        # y轴

plt.subplot2grid((2, 3), (1, 0), colspan=2)         # colspa跨越的列数
data.Age[data.Pclass == 1].plot(kind='kde')         # 从年龄表中抽出
data.Age[data.Pclass == 2].plot(kind='kde')
data.Age[data.Pclass == 3].plot(kind='kde')
plt.xlabel("年龄")
plt.ylabel("密度")
plt.title("各等级的乘客年龄分布")
plt.legend(('1等舱', '2等舱', '3等舱'), loc='best')

plt.subplot2grid((2, 3), (1, 2))
data.Embarked.value_counts().plot(kind='bar')
plt.title("各登船口岸上船人数")
plt.ylabel("人数")
plt.show()

# 看看各乘客等级的获救情况
fig = plt.figure(figsize=(5, 5))
fig.set(alpha=0.2)      # 设定图表颜色alpha参数
# 利用布尔过滤的方法，从乘客等级列表中抽取生还者和遇难者，再进行统计各等级乘客的生还者个数
Survived_0 = data.Pclass[data.Survived == 0].value_counts()
Survived_1 = data.Pclass[data.Survived == 1].value_counts()
df = pd.DataFrame({'获救': Survived_1, '未获救': Survived_0})
df.plot(kind='bar', stacked=True)
plt.title("各乘客等级的获救情况")
plt.xlabel("乘客等级")
plt.ylabel('人数')
plt.show()

# 看看各登录港口的获救情况
fig = plt.figure()
fig.set(alpha=0.2)      # 设定图表颜色alpha参数
Survived_0 = data.Embarked[data.Survived == 0].value_counts()
Survived_1 = data.Embarked[data.Survived == 1].value_counts()
df = pd.DataFrame({u'获救': Survived_1, u'未获救': Survived_0})
df.plot(kind='bar', stacked=True)
plt.title(u"各登录港口乘客的获救情况")
plt.xlabel(u"登录港口")
plt.ylabel(u"人数")
plt.show()

fig = plt.figure()
fig.set(alpha=0.2)      # 设定图表颜色alpha参数
Survived_m = data.Embarked[data.Sex == 'male'].value_counts()
Survived_f = data.Embarked[data.Sex == 'female'].value_counts()
df = pd.DataFrame({u'男性': Survived_m, u'女性': Survived_f})
df.plot(kind='bar', stacked=True)
plt.title(u"按性别看获救情况")
plt.xlabel(u"性别")
plt.ylabel(u"人数")
plt.show()