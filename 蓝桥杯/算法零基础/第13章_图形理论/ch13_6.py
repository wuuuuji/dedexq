def bfs(graph, start):
    """ 广度优先搜寻法 """
    visited = []  # 拜访过的顶点
    queue = [start]  # 仿真队列
    while queue:
        node = queue.pop(0)  # 取索引0的值
        visited.append(node)  # 加入已拜访行列
        neighbors = graph[node]  # 取得已拜访节点的相邻节点
        for n in neighbors:
            queue.append(n)
    return visited


graph = {'A': ['B', 'C', 'D'],
         'B': ['E'],
         'C': ['F'],
         'D': ['G', 'H'],
         'E': [],
         'F': ['I', 'J'],
         'G': [],
         'H': [],
         'I': [],
         'J': []
         }
print(bfs(graph, 'A'))
