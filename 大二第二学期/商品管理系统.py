import json

def login():
    a = input("请输入账号").split()
    b = input("请输入密码").split()
    if a == "admin":
        if b == "123":
            print("登陆成功")
            return 1
        else:
            print("账号，密码有误")
            return 0
    elif a == "user":
        if b == "123":
            print("登陆成功")
            return 2
        else:
            print("账号，密码有误")
            return 0
    else:
        print("账号，密码有误")
        return 0

def admininterface():
    print("\n\n\n\n")
    print("**************************")
    print("********商品管理系统********")
    print("********1.添加商品*********")
    print("********2.查询商品*********")
    print("********3.修改产品*********")
    print("********4.删除产品*********")
    print("********0.退出系统*********")
    print("**************************")
    while True:
        try:
            a = int(input("输入数字进入相应系统"))
            break
        except:
            print("请输入数字。如像添加商品，输入1即可。")
    return a

def userinterface():
    print("\n\n\n\n")
    print("**************************")
    print("********商品管理系统********")
    print("********1.查询商品*********")
    print("********0.退出系统*********")
    print("**************************")
    while True:
        try:
            a = int(input("输入数字进入相应系统"))
            break
        except:
            print("请输入数字。如像添加商品，输入1即可。")
    return a

def system(a, user):
    if user == 1 and (0 <= a <= 4):
        if a == 1:
            addsystem()
            system(admininterface(),1)
        elif a == 2:
            checksystem()
            system(admininterface(),1)
        elif a == 3:
            designsystem()
            system(admininterface(),1)
        elif a == 4:
            delsystem()
            system(admininterface(),1)
        elif a == 0:
            print("感谢使用吴锦斌的商品管理系统")

    elif user == 2 and (0 <= a <= 2):
        if a == 1:
            checksystem()
            system(userinterface(),2)
        elif a == 0:
            print("感谢使用吴锦斌的商品管理系统")
    else:
        print("请输入界面可选择的系统的编号")

def addsystem():
    product = input('请输入商品名称：').strip()
    count = input('请输入商品数量：').strip()
    price = input('请输入商品价格：').strip()
    filename = 'D:\learn\大二第二学期\goods.json'

    try:
        with open(filename, "a+", encoding="UTF-8") as f_obj:
            pass
    except:
        pass


def checksystem():
    pass

def designsystem():
    pass

def delsystem():
    pass

def main():
    a = login()
    if a == 1:
        system(admininterface(),1)
    elif a == 2:
        system(userinterface(),2)
    elif a == 0:
        pass
    else:
        print("系统错误")

main()