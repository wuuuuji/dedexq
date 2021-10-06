import pandas as pd
s1 = pd.Series([1, -2, 2.3, 'hp'])
va1 = s1.values     # 获取值
in1 = s1.index     # 获取索引
print(va1)      # [1 -2 2.3 'hp']
print(in1)     # RangeIndex(start=0, stop=4, step=1)

va2 = list(va1)
in2 = list(in1)