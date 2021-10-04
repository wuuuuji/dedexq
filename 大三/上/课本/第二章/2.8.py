# 数组形态变化
import numpy as np

arr = np.arange(12)
arr1 = arr.reshape(4, 3, order='c')
# 将一维数组转为二维数组
arr2 = arr1.ravel()
# 将二维数组转为一维数组



