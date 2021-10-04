import numpy as np
import matplotlib.pyplot as plt

d1 = [1, 2, 3, 4, 0.1, 7]
d3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
d11 = np.array(d1)
d31 = np.array(d3)
del d1, d3
s11 = d11.shape
print(s11)
s31 = d31.shape
print(s31)

