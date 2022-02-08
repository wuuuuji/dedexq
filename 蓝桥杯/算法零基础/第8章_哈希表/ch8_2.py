phone_book = {}
phone_book['Trump'] = '0912111111'
phone_book['Lisa'] = '0922222222'
phone_book['Mike'] = '0932333333'
name = input('请输入名字 : ')
if name in phone_book:
    print('{} 的电话号码是 {}'.format(name, phone_book[name]))
else:
    print('{} 不在通讯簿内 '.format(name))