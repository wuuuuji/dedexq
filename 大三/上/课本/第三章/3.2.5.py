# 序列聚合运算
import pandas as pd
s = pd.Series([1, 2, 4, 5, 6, 7, 8, 9, 10])
su = s.sum()    # 求和
sm = s.mean()   # 求平均值
ss = s.std()    # 求标准差
smx = s.max()   # 求最大值
smi = s.min()   # 求最小值