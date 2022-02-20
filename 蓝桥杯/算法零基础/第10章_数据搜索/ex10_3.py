def binary_search(Ndict: dict, n):
    for i in Ndict.keys():
        if i == n:
            return i
    return -1


employer = {19: 'John',
            32: 'Tom',
            28: 'Kevin',
            99: 'Curry',
            10: 'Peter'}
n = eval(input("请输入得奖号码 : "))
rtn = binary_search(employer, n)
if rtn != -1:
    print("得奖者是 : ", employer[rtn])
else:
    print("我们小组没人获奖")