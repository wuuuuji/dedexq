def get_edges(graph):
    n1 = []
    n2 = []
    weight = []
    for i in graph:
        for j in graph[i]:
            if graph[i][j] != 0:
                weight.append(graph[i][j])
                n1.append(i)
                n2.append(j)
    return n1, n2, weight


def bellman_ford(graph, start):
    n1, n2, weight = get_edges(graph)
    nodes = dict((i, INF) for i in graph)
    nodes[start] = 0
    for times in range(len(graph) - 1):
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]
            if new_cost < nodes[n2[i]]:
                nodes[n2[i]] = new_cost
                cycle = 1
        if cycle == 0:
            break
    flag = 0

    for i in range(len(nodes)):
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:
        return '图形含负权重的循环'
    return nodes


INF = 999
graph = {'A': {'A': 0, 'B': -1, 'C': 4},
         'B': {'B': 0, 'C': 3, 'D': 2, 'E': 2, 'H': 4},
         'C': {'C': 0},
         'D': {'D': 0, 'B': 1, 'C': 5, 'G': 4},
         'E': {'E': 0, 'D': -3, 'G': 2},
         'G': {'G': 0, 'H': -1},
         'H': {'H': 0, 'G': 3}}
rtn = bellman_ford(graph, 'A')
print(rtn)