from pprint import pp

maze = [  # 迷宫地图
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
directions = [  # 使用列表设计走迷宫方向
    lambda x, y: (x - 1, y),  # 往上走
    lambda x, y: (x + 1, y),  # 往下走
    lambda x, y: (x, y - 1),  # 往左走
    lambda x, y: (x, y + 1)  # 往右走
]


def maze_solve(x, y, goal_x, goal_y):
    '''解迷宫程序 x, y是迷宫入口, goal_x, goal_y是迷宫出口'''
    maze[x][y] = 2
    stack = []  # 建立路线栈
    stack.append((x, y))  # 将路径push入栈
    print("迷宫开始")
    while len(stack) > 0:
        cur = stack[-1]  # 目前位置
        if cur[0] == goal_x and cur[1] == goal_y:
            print('抵达出口')
            return True     # 抵达出口返回True
        for dir in directions:      # 依上、下、左、右优先次序走次迷宫
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:      # 如果是通道就能走
                stack.append(next)
                maze[next[0]][next[1]] = 2      # 用2标记走过的路
                break
        else:
            maze[cur[0]][cur[1]] = 3
            stack.pop()
    else:
        print("没有路径")
        return False

maze_solve(1, 1, 8, 2)
pp(maze)
