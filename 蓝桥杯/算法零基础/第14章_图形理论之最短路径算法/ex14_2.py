def dijkstra(graph, start):
    visited = []
    index = start
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0

    while len(visited) < len(graph):
        visited.append(index)
        for i in graph[index]:
            new_cost = nodes[index] + graph[index][i]
            if new_cost < nodes[i]:
                nodes[i] = new_cost

        next = INF
        for n in nodes:
            if n in visited:
                continue
            if nodes[n] < next:
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
start = input("请输入起点 : ")
rtn = dijkstra(graph, start)
print(rtn)