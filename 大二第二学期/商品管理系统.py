product_list = []
product_name = ["名称:", "编号:", "价格:", "数量:"]


def login():  # 账号验证功能
    a = input("请输入账号：")
    b = input("请输入密码：")
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


def admininterface():  # 管理人员界面
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
            a = int(input("输入数字进入相应系统："))
            break
        except:
            print("请输入数字。如像添加商品，输入1即可。")
    return a


def userinterface():  # 用户界面
    print("\n\n\n\n")
    print("**************************")
    print("********商品管理系统********")
    print("********1.查询商品*********")
    print("********0.退出系统*********")
    print("**************************")
    while True:
        try:
            a = int(input("输入数字进入相应系统："))
            break
        except:
            print("请输入数字。如像添加商品，输入1即可。")
    return a


def system(a, user):  # 跳转系统
    if user == 1 and (0 <= a <= 4):
        if a == 1:
            addsystem()
            system(admininterface(), 1)
        elif a == 2:
            checksystem()
            system(admininterface(), 1)
        elif a == 3:
            designsystem()
            system(admininterface(), 1)
        elif a == 4:
            delsystem()
            system(admininterface(), 1)
        elif a == 0:
            print("感谢使用吴锦斌的商品管理系统")

    elif user == 2 and (0 <= a <= 2):
        if a == 1:
            checksystem()
            system(userinterface(), 2)
        elif a == 0:
            print("感谢使用吴锦斌的商品管理系统")
    else:
        print("请输入界面可选择的系统的编号")


def addsystem():  # 添加系统
    numbers = input("请输入商品编号：").strip()
    product = input('请输入商品名称：').strip()
    count = input('请输入商品数量：').strip()
    price = input('请输入商品价格：').strip()
    filename = 'goods.txt'
    with open(filename, "a+", encoding="UTF-8") as f_obj:
        if product == '':
            print('商品名称不能为空')
        elif not count.isdigit():
            print('商品数量必须为正整数')
        elif not float(price) >= 0:
            print('商品价格必须为正数')
        else:
            f_obj.seek(0)
            product_dict = {
                "名称": product,
                "编号": numbers,
                "数量": count,
                "价钱": price
            }
            product_list.append(product_dict)
            for i in product_list:
                for j, k in i.items():
                    f_obj.write(j + ":" + str(k))
                    f_obj.write("   ")
                f_obj.write("\n")
            print("添加'" + product + "'成功，价格为" + price + "元，数量为" + count)


def checksystem():  # 查询系统
    filename = 'goods.txt'
    with open(filename, "r", encoding="UTF-8") as f_obj:
        print("""
           产品信息如下：\n
产品名称		编号	    数量	    价格(元)
            """)
        for line in f_obj.readlines():
            line = line.strip()
            print(line)


def designsystem():  # 修改系统
    filename = 'goods.txt'
    a = input("输入编号，确定要修改的商品")
    b = "编号:" + a
    lines = []

    def design_goods(line):
        list_words = line.split()
        print("1.产品名称  2.数量  3.价格  0.退出")
        stnumber = int(input("请输入数字选择你要的操作:"))
        if stnumber <= 0:
            print("请输入正整数")
        elif not 0 <= stnumber <= 3:
            print("请输入正确的数字操作")
        elif stnumber == 0:
            pass
        else:
            a = input("输入你修改后的值")
            if stnumber == 1:
                list_words[0] = "名称:" + a
            elif stnumber == 2:
                list_words[2] = "数量:" + a
            elif stnumber == 3:
                list_words[3] = "价钱:" + a
        str_words = "\t".join(list_words)
        return str_words

    with open(filename, "r", encoding="UTF-8") as f_obj:
        for line in f_obj.readlines():
            if line != "\n":
                lines.append(line)
        f_obj.close()

    with open(filename, "w", encoding="UTF-8") as f:
        for line in lines:
            if b in line:
                line = design_goods(line);
                f.write("%s\n" % line)
            else:
                f.write("%s" % line)


def delsystem():
    print("1.产品名称  2.数量  3.价格  0.退出")
    while True:
        do_number = input("请输入你要选择的操作：")
        if do_number.isdigit():
            do_number = int(do_number)
            if 0 < do_number < 4:
                do_name = input("具体的值是：")
                break

    def switch(do_number, do_name):
        for i in product_list:
            if i[product_name[do_number - 1]] == do_name:  # 遍历列表中的字典的值与之作比较
                product_list.remove(i)
                print("删除成功！")

    switch(do_number, do_name)


def main():
    a = login()
    if a == 1:
        system(admininterface(), 1)
    elif a == 2:
        system(userinterface(), 2)
    elif a == 0:
        pass
    else:
        print("系统错误")


main()
