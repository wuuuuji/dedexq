def hanoi(n, src, aux, dst):
    global step
    '''河内塔'''
    if n == 1:      # 河内塔终止条件
        step += 1   # 记录步骤
        print('{0:2d} : 移动圆盘 {1} 从 {2} 到 {3}'.format(step, n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        step += 1
        print('{0:2d} : 移动圆盘 {1} 从 {2} 到 {3}'.format(step, n, src, dst))
        hanoi(n - 1, aux, src, dst)


step = 0
n = eval(input("请输入圆盘数量 : "))
hanoi(n, 'A', 'B', 'C')