# 数组的连接
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C_s = np.hstack((A, B))
# 横向拼接
C_v = np.vstack((A, B))
# 纵向拼接