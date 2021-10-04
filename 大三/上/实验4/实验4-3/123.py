import pandas as pd

erol2 = pd.read_csv('./data/Euro2012.csv')
erol2['Goals']
# 单列 或 多列 数据访问
# 索引与切片区别
# iloc 与loc区别
# 3. 有多少球队参与了2012欧洲杯？
erol2['Team'].nunique()
# 4. 该数据集中一共有多少列(columns)?
erol2.shape[1]
# 5. 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框。
discipline=erol2[['Team','Yellow Cards','Red Cards']]
# 6. 对数据框discipline按照先Red Cards再Yellow Cards进行排序。
discipline.sort_values(by=['Red Cards','Yellow Cards'])
# 7. 计算每个球队拿到的黄牌数的平均值。
discipline.groupby('Team').agg({'Yellow Cards':'mean'})
# 8. 找到进球数Goals超过6的球队数据。
index=erol2['Goals']>6
erol2.loc[index,:]
# 9. 选取以字母G开头的球队数据。
s2=erol2['Team'].str[0]=='G'
erol2.loc[s2,:]
# 10.选取前7列。
erol2.iloc[:,0:7]
# 11.选取除了最后3列之外的全部列。
erol2.iloc[:,0:-3]
# 左闭右开
# 12.找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)。
erol2.loc[erol2.Team.isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]