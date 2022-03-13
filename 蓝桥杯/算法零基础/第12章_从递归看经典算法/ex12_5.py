def hanoi(n, src, aux, dst):
    if n == 1:
        print('移动圆盘 {} 从 {} 到 {}'.format(n, src, dst))
    else:
        hanoi(n - 1, src, dst, aux)
        print('移动圆盘 {} 从 {} 到 {}'.format(n, src, dst))
        hanoi(n - 1, aux, src, dst)


n = eval(input("请输入圆盘数量 : "))
hanoi(n, 'A', 'C', 'B')