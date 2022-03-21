def dijkstra(graph, start):
    visited = []
    index = start
    nodes = dict((i, INF) for i in graph)   # 设定节点为最大值
    nodes[start] = 0    # 设定起点为start

    while len(visited) < len(graph):    # 有几个节点就执行几次
        visited.append(index)
        for i in graph[index]:
            new_cost = nodes[index] + graph[index][i]   # 新路径距离
            if new_cost< nodes[i]:  # 新路径如果比较段
                nodes[i] = new_cost     # 采用新路径

        next = INF
        for n in nodes:  # 从列表中找出下一个节点
            if n in visited:    # 如果已拜访回到for选下一个
                continue
            if nodes[n] < next: # 找出新的最小权重节点
                next = nodes[n]
                index = n
    return nodes


INF = 9999
graph = {'A': {'A': 0, 'B': 2, 'C': 4},
         'B': {'B': 0, 'C': 7, 'E': 6},
         'C': {'C': 0, 'D': 6, 'E': 2},
         'D': {'D': 0, 'E': 8, 'G': 4},
         'E': {'E': 0, 'G': 2},
         'G': {'G': 0}
         }
rtn = dijkstra(graph, 'A')
print(rtn)