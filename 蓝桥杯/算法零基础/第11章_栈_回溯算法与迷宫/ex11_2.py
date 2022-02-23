from pprint import pp

maze = [
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
directions = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def maze_solve(x, y, goal_x, goal_y):
    maze[x][y] = 2
    stack = []
    stack.append((x, y))
    print("迷宫开始")
    while len(stack) > 0:
        cur = stack[-1]
        if cur[0] == goal_x and cur[1] == goal_y:
            print('抵达出口')
            return True
        for dir in directions:
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:
            maze[cur[0]][cur[1]] = 3
            stack.pop()
    else:
        print("没有路径")
        return False


print("迷宫图形如下 : ")
pp(maze)
entry_x, entry_y = eval(input("请输入迷宫入口 x, y : "))
exit_x, exit_y = eval(input("请输入迷宫出口 x, y : "))
maze_solve(entry_x, entry_y, exit_x, exit_y)
pp(maze)