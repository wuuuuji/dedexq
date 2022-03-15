def is_exit(node):
    """ 回应是否出口 """
    if node == 'K':
        return True

def bfs(graph, start):
    """ 广度优先搜寻法 """
    global visited      # 拜访过的顶点
    queue = [start]     # 仿真队列
    while queue:
        node = queue.pop(0)     # 取索引0的值
        if is_exit(node):       # 如果是True，表示找到了
            print(node + '是迷宫出口')
            visited.append(node)    # 将出口加入已拜访
            return visited          # bfs()执行结束
        if node not in visited:
            visited.append(node)    # 加入已拜访行列
            neighbors = graph[node]     # 取得已拜访节点的相邻节点
            for n in neighbors:     # 将相邻节点放入队列
                queue.append(n)
    return visited


graph = {'A': ['B'],
         'B': ['A', 'C'],
         'C': ['B', 'D', 'E'],
         'D': ['C'],
         'E': ['C', 'H'],
         'F': ['G'],
         'G': ['F', 'H', 'J'],
         'H': ['E', 'G', 'I'],
         'I': ['H', 'K'],
         'J': ['G'],
         'K': ['I']
         }
visited = []
print(bfs(graph, 'A'))