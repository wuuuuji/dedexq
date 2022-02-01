def bye():
    print("下回见！")


def system(name):
    print("%s 欢迎进入第二层" % name)


def welcome(name):
    print("%s 欢迎进入第一层" % name)
    system(name)
    print("欢迎下次使用")
    bye()


welcome("吴锦斌")
