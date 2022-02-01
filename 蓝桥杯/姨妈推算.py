import datetime


def inputdate():
    indate = input("请输入日期（如20210101）：")
    indate = indate.strip()
    datestr = indate[0:4] + "-" + indate[4:6] + "-" + indate[6:]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')


if __name__ == '__main__':
    print("---------推算几天后的日期---------")
    sdate = inputdate()
    in_num = int(input("请输入间隔的天数："))
    for i in range(1, 4):
        fdate = sdate + datetime.timedelta(days=in_num*i)
        print(f"您推算的日期是：{str(fdate)}")