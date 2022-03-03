def mycount(NList):
    if not NList:
        return 0
    return 1 + mycount(NList[1:])


data = [1, 5, 9, 2, 8, 100, 81]
print('data       = ', data)
print("data元素个数 = ", mycount(data))