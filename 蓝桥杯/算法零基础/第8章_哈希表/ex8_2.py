def check_name(name):
    if voted.get(name):
        print('你已经投过票了')
    else:
        print('欢迎投票')
        voted[name] = True


voted: dict = {}

name = input('请输入名字 : ')
check_name(name)
