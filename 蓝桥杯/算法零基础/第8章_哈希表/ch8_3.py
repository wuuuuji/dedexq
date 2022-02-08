def check_name(name):
    if voted[name]:
        print('你已经投过票了')
    else:
        print('欢迎投票')
        voted[name] = True


voted = {'Trump': None,
         'Lisa': None,
         'Mike': None}

name = input('请输入名字 : ')
if name in voted:
    check_name(name)
else:
    print('你不是选民')
