import numpy as np
import matplotlib.pyplot as plt

def length(x1, y1, x2, y2):
    ''' 计算2点之间的距离 '''
    return int(((x1-x2)**2 + (y1-y2)**2)**0.5)

def clustering(x, y, cx, cy):
    ''' 对元素执行分群 '''
    clusters = []
    for i in range(cluster_number):                 # 建立群集
        clusters.append([])
    for i in range(seeds):                          # 为每个点找群集
        distance = INF                              # 设定最初距离
        for j in range(cluster_number):             # 计算每个点与群集中心的距离
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j                   # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])    # 此点加入此索引的群集
    return clusters

def kmeans(x, y, cx, cy):
    ''' 建立群集和绘制各群集点和线条'''
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color='b')                        # 绘制元素点
    plt.scatter(cx, cy, color='r')                      # 用红色绘群集中心

    c = ['r', 'g', 'y']                                 # 群集的线条颜色
    for index, node in enumerate(clusters):             # 为每个群集中心建立线条
        linex = []                                      # 线条的 x 坐标
        liney = []                                      # 线条的 y 坐标
        for n in node:
            linex.append([n[0], cx[index]])             # 建立线条x坐标列表
            liney.append([n[1], cy[index]])             # 建立线条y坐标列表
        color_c = c[index]                              # 选择颜色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c) # 为第i群集绘线条
    plt.show()
    return clusters

def get_new_cluster(clusters):
    ''' 计算各群集中心的点 '''
    new_x = []                                          # 新群集中心 x 坐标
    new_y = []                                          # 新群集中心 y 坐标
    for index, node in enumerate(clusters):             # 逐步计算各群集
        nx, ny = 0, 0
        for n in node:
            nx += n[0]
            ny += n[1]
        new_x.append([])
        new_x[index] = int(nx / len(node))              # 计算群集中心 x 坐标
        new_y.append([])
        new_y[index] = int(ny / len(node))              # 计算群集中心 y 坐标
    return new_x, new_y

# 群集中心, 元素的数量, 数据最大范围
INF = 999                                               # 假设最大距离
cluster_number = 3                                      # 群集中心数量
seeds = 50                                              # 元素数量
limits = 100                                            # 值在(100, 100)内
# 使用随机数建立seeds数量的种子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用随机数建立cluster_number数量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

clusters = kmeans(x, y, cluster_x, cluster_y)

while True:                                             # 收敛循环
    new_x, new_y = get_new_cluster(clusters)
    x_list = list(cluster_x)                            # 将np.array转成列表
    y_list = list(cluster_y)                            # 将np.array转成列表
    if new_x == x_list and new_y == y_list:             # 如果相同代表收敛完成
        break
    else:
        cluster_x = new_x                               # 否则重新收敛
        cluster_y = new_y
        clusters = kmeans(x, y, cluster_x, cluster_y)