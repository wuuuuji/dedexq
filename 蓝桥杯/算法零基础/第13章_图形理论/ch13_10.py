"""
深度优先搜寻法(无向图)
"""

def dfs(graph, node, path=None):
    """ 深度优先搜寻法 """
    if path is None:
        path = []
    path += [node]      # 路径
    for n in graph[node]:   # 将相邻节点放入队列
        if n not in path:
            path = dfs(graph, n, path)
        return path


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
print(dfs(graph, 'A'))
