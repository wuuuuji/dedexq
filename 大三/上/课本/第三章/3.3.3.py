# 数据框基础方法

import pandas as pd
import numpy as np

data = {'a': [2, 2, np.nan, 5, 6],
        'b': ['k1', 'k1', 'k1', np.nan, 'k1'],
        'c': [4, 6, 5, np.nan, 6],
        'd': [7, 9, np.nan, 9, 8]}
df = pd.DataFrame(data)

# dropna()
# 去掉空值
df1 = df.dropna()