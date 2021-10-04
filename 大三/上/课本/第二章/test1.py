import numpy as np

list1 = [1, 2, 4, 6, 7, 8]
N1 = np.array(list1, dtype="int8")

tup1 = (1, 2, 3, 4, 5, 6)
N2 = np.array(tup1, dtype="int8")

N3 = np.ones([1, 6], dtype="int8")

N4 = np.vstack((N1, N2, N3))

np.save("123", N4)