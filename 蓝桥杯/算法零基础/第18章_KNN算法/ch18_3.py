import numpy as np
import matplotlib.pyplot as plt


def kmeans(x, y, cx, cy):
    ''' 目前功能只是绘群集元素点 '''
    plt.scatter(x, y, color='b')  # 绘制元素点
    plt.scatter(cx, cy, color='r')  # 用红色绘群集中心
    plt.show()


# 群集中心, 元素的数量, 数据最大范围
cluster_number = 3  # 群集中心数量
seeds = 50  # 元素数量
limits = 100  # 值在(100, 100)内
# 使用随机数建立seeds数量的种子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用随机数建立cluster_number数量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)