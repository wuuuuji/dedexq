import numpy as np

N4 = np.load('123.npy')

a = N4[0, [1, 3]]
b = N4[2, [0, 4]]
N5 = np.hstack((a, b))

list1 = [1, 2, 4, 6, 7, 8]
N1 = np.array(list1, dtype="int8")
N6 = np.hstack((N1,N5))