# 序列方法

import pandas as pd
import numpy as np

# unique()
# 去掉序列中重复的元素值
s5 = [1, 2, 2, 3, 'hp', 'hp', 'he']
s5 = pd.Series(s5)
s51 = s5.unique()
print(s51)

print("\n\n\n")

# isin()
# 判断元素值的存在性
s52 = s5.isin([0, 'he'])
print(s52)


print("\n\n\n")

# value_counts()
# 统计序列元素值出现的次数
s53 = s5.value_counts()
print(s53)


print("\n\n\n")

# 空值的处理
"""
isnull()判断是否有空值，有返回true
notnull()判断是否非空值，是非空，返回true
dropan()清洗序列中的空值
"""
ss1 = pd.Series([10, 'hp', 60, np.nan ,20])     # np.nan意思是空值
tt1 = ss1[~ss1.isnull()]
print(tt1)
tt2 = ss1[ss1.notnull()]
print(tt2)
tt3 = ss1.dropna()
print(tt3)