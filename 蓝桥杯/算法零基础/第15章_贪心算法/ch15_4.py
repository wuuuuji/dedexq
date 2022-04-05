def greedy(graph1: list, cities1: list, start: str):
    visited = []    # 存储已拜访城市
    visited.append(start)   # 存储起点城市
    start_i = cities1.index(start)   # 获得起点城市的索引
    distance = 0    # 旅行距离
    for outer in range(len(cities1) - 1):    # 寻找最近城市
        graph1[start_i][start_i] = INF  # 将自己城市距离设为极大值
        min_dist = min(graph1[start_i])     # 找出最短路径
        distance += min_dist    # 更新总路程距离
        end_i = graph1[start_i].index(min_dist)     # 最短距离城市的索引
        visited.append(cities1[end_i])      # 将最短距离城市列入已拜访
        for inner in range(len(graph1)):
            graph1[start_i][inner] = INF
            graph1[inner][start_i] = INF
        start_i = end_i
    return distance, visited


INF = 9999
cities = ['新竹', '竹南', '竹北', '关西', '竹东']
graph = [[0, 12, 10, 28, 16],
         [12, 0, 20, 35, 19],
         [10, 20, 0, 21, 11],
         [28, 35, 21, 0, 12],
         [16, 19, 11, 12, 0]]
dist, visited = greedy(graph, cities, '新竹')
print('拜访顺序: ', visited)
print('拜访距离: ', dist)
