# 序列切片
import pandas as pd
import numpy as np

s1 = pd.Series([1, -2, 2.3, 'hp'])
s2 = pd.Series([1, -2, 2.3, 'hp'], index=['a', 'b', 'c', 'd'])
s4 = pd.Series(np.array([1, 2, 4, 7, 11]))
s22 = s2[['a', 'd']]
s11 = s1[0:2]
s12 = s1[[0, 2, 3]]
s41 = s4[s4 > 2]
print(s22)
print('-'*20)
print(s11)
print('-'*20)
print(s12)
print('-'*20)
print(s41)