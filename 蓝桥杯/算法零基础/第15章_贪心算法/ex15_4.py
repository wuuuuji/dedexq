def greedy(graph1: list, cities1: list, start: str):
    visited = []
    visited.append(start)
    start_i = cities1.index(start)
    distance = 0
    for outer in range(len(cities1) - 1):
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
cities = ['新竹', '竹南', '竹北', '关西', '竹东']
graph = [[0, 12, 10, 28, 16],
         [12, 0, 20, 35, 19],
         [10, 20, 0, 21, 11],
         [28, 35, 21, 0, 12],
         [16, 19, 11, 12, 0]]
a = input("请输入开始城市起点: ")
dist, visited = greedy(graph, cities, a)
print('拜访顺序: ', visited)
print('拜访距离: ', dist)