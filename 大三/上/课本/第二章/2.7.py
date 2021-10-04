# 数据春秋
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C_s = np.hstack((A, B))
np.save('data', C_s)
# 将数据集存储到data.npy中
C_l = np.load('data.npy')
print(C_l)