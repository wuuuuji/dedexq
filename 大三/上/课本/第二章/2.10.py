import numpy as np

mat1 = np.mat("1 2 3; 4 5 6; 7 8 9")
mat2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr1 = np.eye(3, dtype="int8")
arr2 = 3*arr1
mat = np.bmat("arr1 arr2;arr1 arr2")

mat3 = np.matrix(np.arange(4).reshape(2, 2))
mT = mat3.T
# 返回矩阵的转置
mH = mat3.H
# 返回矩阵的共轭矩阵
mI = mat3.I
# 返回矩阵的逆矩阵
