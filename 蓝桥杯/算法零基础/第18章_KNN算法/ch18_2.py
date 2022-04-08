import math


def knn(record, target, k):
    ''' 计算k组近邻值, 以list回传数量和距离 '''
    distances = []  # 储存纪录与目标的距离
    record_number = []  # 储存纪录的烤香肠数量

    for r in record:  # 计算过往纪录与目标的距离
        tmp = 0
        for i in range(len(target) - 1):
            tmp += (target[i] - r[i]) ** 2
        dist = math.sqrt(tmp)
        distances.append(dist)  # 储存距离
        record_number.append(r[len(target) - 1])  # 储存烤香肠数量

    knn_number = []  # 储存k组烤香肠数量
    knn_distances = []  # 储存k组距离值
    for i in range(k):  # k代表取k组近邻值
        min_value = min(distances)  # 计算最小值
        min_index = distances.index(min_value)  # 计算最小值索引
        # 将香肠数量分别储存至knn_number列表
        knn_number.append(record_number.pop(min_index))
        # 将距离分别储存至knn_distances
        knn_distances.append(distances.pop(min_index))
    return knn_number, knn_distances


def regression(knn_num):
    ''' 计算回归值 '''
    return int(sum(knn_num) / len(knn_num))


target = [1, 5, 2, 'value']  # value是需计算的值
# 过往纪录
record = [
    [0, 3, 3, 100],
    [2, 4, 3, 250],
    [2, 5, 6, 350],
    [1, 4, 2, 180],
    [2, 3, 1, 170],
    [1, 5, 4, 300],
    [0, 1, 1, 50],
    [2, 4, 3, 275],
    [2, 2, 4, 230],
    [1, 3, 5, 165],
    [1, 5, 5, 320],
    [2, 5, 1, 210],
]

k = 5  # 设定k组最相邻的值
k_nn = knn(record, target, k)
print("需准备 %d 条烤香肠" % regression(k_nn[0]))
for i in range(k):
    print("k组近邻的距离 %6.4f, 销售数量 %d" % (k_nn[1][i], k_nn[0][i]))