phone_number = {'Emergency': 119}

num = input("请输入名字 : ")
if num in phone_number:
    print('{} 的电话号码是 {}'.format(num, phone_number[num]))
else:
    print('{} 不在通讯簿内 '.format(num))