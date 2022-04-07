def greedy(graph1: list, cities1: list, start: str):
    visited = []
    visited.append(start)
    start_i = cities1.index(start)
    distance = 0
    for out in range(len(cities1) - 1):
        graph1[start_i][start_i] = INF
        min_dist = min(graph1[start_i])
        distance += min_dist
        end_i = graph1[start_i].index(min_dist)
        visited.append(cities1[end_i])
        for inner in range(len(graph1)):
            graph1[start_i][inner] = INF
            graph1[inner][start_i] = INF
        start_i = end_i
    return distance, visited


INF = 9999
cities = ['北京', '天津', '西安', '武汉', '上海', '广州']
graph = [[0, 132, 1120, 1200, 1463, 1888],
         [132, 0, 1182, 1367, 957, 2100],
         [1120, 1182, 0, 1035, 1509, 1950],
         [1200, 1367, 1035, 0, 686, 1030],
         [1463, 957, 1509, 686, 0, 1705],
         [1888, 2100, 1950, 1030, 1705, 0]
         ]
a = input('请输入开始城市起点: ')
dist, visited = greedy(graph, cities, a)
print('拜访顺序: ', visited)
print('拜访距离: ', dist)