data = []
while True:
    val = input("请输入数值(Q或q代表输入结束) : ")
    if val == 'Q' or val == 'q':
        break
    data.append(val)
max = data[0]
for num in data:
    if num > max:
        max = num
print("最大值 : ", max)