# 数据框基础方法

import pandas as pd
import numpy as np

data = {'a': [2, 2, np.nan, 5, 6],
        'b': ['k1', 'k1', 'k1', np.nan, 'k1'],
        'c': [4, 6, 5, np.nan, 6],
        'd': [7, 9, np.nan, 9, 8]}
df = pd.DataFrame(data, dtype='int8')

# dropna()
# 去掉有空值的哪一行
df1 = df.dropna(thresh=3, subset=['a', 'd'])
df2 = df.dropna(thresh=1, subset=['a', 'd'])

# fillna()
df2 = df.fillna(0)
df3 = df.fillna('K1')
df4 = df.fillna({"a": 0, "b": 'k1', "c": 0, "d": 0})
# 给a，c，d列的空值赋值0，给b列的空值赋值k1
df5 = df.fillna({"a": 0, "b": 'k1'})
# 给a列的空值赋值0，给b列的空值赋值k1

# sort_values()
data = {'a': [5, 3, 4, 1, 6],
        'b': ['d', 'c', 'a', 'e', 'q'],
        'c': [4, 6, 5, 5, 6]}
Df = pd.DataFrame(data)
Df1 = Df.sort_values(by='a', ascending=False)
# 默认按升序,这里设置为降序

# sort_index()
Df2 = Df1.sort_index(ascending=False)
# 默认按升序,这里设置为降序

# head()
H4 = Df2.head(4);
# 取数据集中的前N行。

# drop()
H41 = H4.drop('b', axis=1)
# 删除数据集中的指定列。

# join()
Df3 = pd.DataFrame({'d': [1,2,3,4,5]})
Df4 = Df.join(Df3)
# 实现两个数据框之间的水平连接

# to_numpy()
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1.4, 3.5, 2, 6, 7, 8]
list4 = [4, 5, 6, 7, 8, 9]
list5 = ['t', 5, 6, 7, 'k', 9.6]
D = {'M1': list1, 'M2': list2, 'M3': list3, 'M4': list4, 'M5': list5}
# 定义字典D，值为字符、数值混合数据
G = {'M1': list1, 'M2': list3, 'M3': list4}
# 定义字典G。值为纯数值数据
D = pd.DataFrame(D)
# 将字典转化数据框
D1 = D.to_numpy()
G = pd.DataFrame(G)
# 将字典转化数据框
G1 = G.to_numpy()

# to_excel()
D.to_excel('D.xlsx')
G.to_excel('G.xlsx')

