# 数据框创建

import pandas as pd
import numpy as np

data = {'a': [2, 2, np.nan, 5, 6],
        'b': ['k1', 'k1', 'k1', np.nan, 'k1'],
        'c': [4, 6, 5, np.nan, 6],
        'd': [7, 9, np.nan, 9, 8]}
df = pd.DataFrame(data)
print(df)
print('-'*50)

print('columns=', end='')
print(df.columns)       # 列名
print('-'*50)

print('index=', end='')
print(df.index)         # 行索引
print('-'*50)

print('values=')
print(df.values)        # 数值
