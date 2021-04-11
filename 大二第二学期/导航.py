def door1():
    print("目前你在东门")
    print("选择你的干饭之路")
    print("(1)一饭 (2)二饭 (3)三饭")
    try:
        eat = int(input("输入数字选择食堂"))
        if eat == 1:
            print("向右走汽车通道到达西门")
            print("向右趴斜坡至顶到达篮球场。在篮球场的旁边就是一饭食堂")
        elif eat == 2:
            print("向右走汽车通道到达西门")
            print("向右趴斜坡至顶，再往前走100米到达凉茶铺。")
            print("凉茶铺向右走100米，到达栋女生宿舍。")
            print("正对女生宿舍门口，向左走30米到达二饭食堂")
        elif eat == 3:
            print("向左沿着电子楼的方向一直往下走，到达三饭食堂")
        else:
            print("请重新输入数字")
    except:
        print("请输入数字。例如去一饭，输入数字1即可")



def door2():
    print("目前你在西门")
    print("选择你的干饭之路")
    print("(1)一饭 (2)二饭 (3)三饭")
    try:
        eat = int(input("输入数字选择食堂"))
        if eat == 1:
            print("向右趴斜坡至顶到达篮球场。在篮球场的旁边就是一饭食堂")
        elif eat == 2:
            print("向右趴斜坡至顶，再往前走100米到达凉茶铺。")
            print("凉茶铺向右走100米，到达栋女生宿舍。")
            print("正对女生宿舍门口，向左走30米到达二饭食堂")
        elif eat == 3:
            print("向左走汽车通道到达东门。")
            print("向左沿着电子楼的方向一直往下走，到达三饭食堂")
        else:
            print("请重新输入数字")
    except:
        print("请输入数字。例如去一饭，输入数字1即可")



def door3():
    print("目前你在桥门")
    print("选择你的干饭之路")
    print("(1)一饭 (2)二饭 (3)三饭")
    try:
        eat = int(input("输入数字选择食堂"))
        if eat == 1:
            print("往前走到达第一个拐角，向右拐，一直走到达东门")
            print("向右走汽车通道到达西门")
            print("向右趴斜坡至顶到达篮球场。在篮球场的旁边就是一饭食堂")
        elif eat == 2:
            print("往前走到达第一个拐角，向右拐，一直走到达东门")
            print("向右走汽车通道到达西门")
            print("向右趴斜坡至顶，再往前走100米到达凉茶铺。")
            print("凉茶铺向右走100米，到达栋女生宿舍。")
            print("正对女生宿舍门口，向左走30米到达二饭食堂")
        elif eat == 3:
            print("往前一直走，到达第一个拐角向右拐走50米，在向左到达三饭食堂")

        else:
            print("请重新输入数字")
    except:
        print("请输入数字。例如去一饭，输入数字1即可")


print("选择你想进入的入口")
print("(0)退出 (1)东门  (2)西门  (3)桥门")
while(1):
    try:
        door = int(input("输入数字选择门口"))
        if door == 1:
            door1()
            break
        elif door == 2:
            door2()
            break
        elif door == 3:
            door3()
            break
        elif door == 0:
            break
        else:
            print("请重新输入数字")
    except:
        print("请输入数字。例如去东门，输入数字1即可")
print("感谢使用无敌简单版校园导航系统")