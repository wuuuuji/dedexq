import pandas as pd
import numpy as np

s1 = pd.Series([1, -2, 2.3, 'hp'], index=['a', 'b', 'c', 'd'], dtype='object', name='123')
s2 = pd.Series([1, -2, 2.3, 'hp'], index=['a', 'b', 'c', 'd'])
s3 = pd.Series((1, -2, 2.3, 'hp'))
s4 = pd.Series(np.array([1, 2, 4, 7.1]))
mydict = {'red': 2000, 'blue': 1000, 'yellow': 500}
ss = pd.Series(mydict)