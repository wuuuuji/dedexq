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

