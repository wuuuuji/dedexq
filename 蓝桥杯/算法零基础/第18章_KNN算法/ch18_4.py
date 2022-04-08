import numpy as np
import matplotlib.pyplot as plt


def length(x1, y1, x2, y2):
    ''' 计算2点之间的距离 '''
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    ''' 对元素执行分群 '''
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 为每个点找群集
        distance = INF  # 设定最初距离
        for j in range(cluster_number):  # 计算每个点与群集中心的距离
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此点加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    ''' 建立群集和绘制各群集点和线条'''
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color='b')  # 绘制元素点
    plt.scatter(cx, cy, color='r')  # 用红色绘群集中心

    c = ['r', 'g', 'y']  # 群集的线条颜色
    for index, node in enumerate(clusters):  # 为每个群集中心建立线条
        linex = []  # 线条的 x 坐标
        liney = []  # 线条的 y 坐标
        for n in node:
            linex.append([n[0], cx[index]])  # 建立线条x坐标列表
            liney.append([n[1], cy[index]])  # 建立线条y坐标列表
        color_c = c[index]  # 选择颜色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 为第i群集绘线条
    plt.show()


# 群集中心, 元素的数量, 数据最大范围
INF = 999  # 假设最大距离
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