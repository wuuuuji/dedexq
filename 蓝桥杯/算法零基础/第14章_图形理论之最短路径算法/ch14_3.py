""" 贝尔曼-富特算法 """
def get_edges(graph):
    n1 = []  # 线段的节点1
    n2 = []  # 线段的节点2
    weight = []  # 定义线段
    for i in graph:  # 为每一个线段建立两端的节点列表
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
    for times in range(len(graph) - 1):  # 执行循环len(graph) - 1
        cycle = 0
        for i in range(len(weight)):
            new_cost = nodes[n1[i]] + weight[i]  # 新的路径花费
            if new_cost < nodes[n2[i]]:  # 如果新路径比较短
                nodes[n2[i]] = new_cost
                cycle = 1  # 采用新路径
        if cycle == 0:
            break
    flag = 0

    # 检查是否存在负权重的循环
    for i in range(len(nodes)):  # 对每条边线再执行一次松弛操作
        if nodes[n1[i]] + weight[i] < nodes[n2[i]]:
            flag = 1
            break
    if flag:  # 如果有变化表示有负权重
        return '图形含负权重的循环'
    return nodes


INF = 999
graph = {'A': {'A': 0, 'B': -1, 'C': 4},
         'B': {'B': 0, 'C': 3, 'D': 2, 'E': 2},
         'C': {'C': 0},
         'D': {'D': 0, 'B': 1, 'C': 5, 'G': 4},
         'E': {'E': 0, 'D': -3, 'G': 2},
         'G': {'G': 0}
         }
rtn = bellman_ford(graph, 'A')
print(rtn)