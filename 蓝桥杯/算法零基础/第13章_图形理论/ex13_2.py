def dfs(graph, start, goal):
    path = []                               # 拜访过的节点
    stack = [start]                         # 仿真堆栈
    while stack:
        node = stack.pop()                  # pop堆栈
        if node in path:
            continue
        path.append(node)                   # 加入已拜访行列
        if node == goal:                    # 如果找到了
            print('找到了')
            return path
        for n in graph[node]:               # 将相邻节点放入队列
            stack.append(n)
    return "找不到"



graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E'],
         'C': ['A', 'F'],
         'D': ['A', 'G', 'H'],
         'E': ['B'],
         'F': ['C', 'I', 'J'],
         'G': ['D'],
         'H': ['D'],
         'I': ['F'],
         'J': ['F'],
         }

print(dfs(graph, 'F', 'G'))