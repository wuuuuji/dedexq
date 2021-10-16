import numpy as np

# 数组的创建
t1 = np.zeros((2,3))
t2 = np.ones((3,4))
t3 = np.random.randint(0,10,(3,2))
# 数组的属性
print("-"*20)
print("第二部分:")
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a.size)
# 数组的维度操作
print("-"*20)
print("第三部分:")
print(a.T)
print("-"*20)
print(a[-1])
print("-"*20)
print(a[2:4])
print("-"*20)
print(a[::-1])
# 数据的合并
print("-"*20)
print("第四部分:")
a4 = np.arange(9).reshape(3,3)
b4 = np.arange(9).reshape(3,3)
print(np.hstack((a4, b4)))     # 水平合并
print("-"*20)
print(np.vstack((a4, b4)))     # 垂直合并
print("-"*20)
print(np.dstack((a4, b4)))     # 深度合并
print("-"*20)
# 数组拆分
print("-"*20)
print("第五部分:")
a5 = np.arange(9).reshape(3,3)
print(np.hsplit(a5 ,3))     # 按列拆分为多个子数组
print(np.vsplit(a5, 3))     # 按行拆分为多个子数组
b5 = np.arange(27).reshape(3,3,3)
print(np.dsplit(b5, 3))     # 将一个数组拆分为多个大小相等的子数组。
# 数组运算
print("-"*20)
print("第六部分:")
a6 = np.arange(4, dtype=np.float32).reshape(2,2)
b6 = np.arange(4,8,dtype=np.float32).reshape(2,2)
print(a6+2)
a6/b6