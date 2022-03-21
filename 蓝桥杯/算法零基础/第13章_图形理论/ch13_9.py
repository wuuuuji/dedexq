"""
深度优先搜寻法(有向图)
"""

def dfs(graph, start, goal):
    """ 深度优先搜寻法 """
    path = []           # 拜访过的节点
    stact = [start]     # 仿真栈
    while stact:
        node = stact.pop()      # pop栈
        path.append(node)       # 加入已拜访行列
        if node == goal:        # 如果找到了
            print('找到了')
            return path
        for n in graph[node]:   # 将相邻节点放入队列
            stact.append(n)
    return '找不到'


graph = {'A': ['D', 'C', 'B'],
         'B': ['E'],
         'C': ['F'],
         'D': ['H', 'G'],
         'E': [],
         'F': ['J', 'I'],
         'G': [],
         'H': [],
         'I': [],
         'J': [],
         }
print(dfs(graph, 'A', 'G'))
