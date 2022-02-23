"""
小蓝每天都锻炼身体。
正常情况下，小蓝每天跑 1 千米。如果某天是周一或者月初（1 日），为了激励自己，小蓝要跑 2 千米。如果同时是周一或月初，小蓝也是跑 2 千米。
小蓝跑步已经坚持了很长时间，从 2000 年 1 月 1 日周六（含）到 2020 年 101 月 1 日周四（含）。请问这段时间小蓝总共跑步多少千米？
"""
import datetime


def run():
    start = datetime.date(2000, 1, 1)
    end = datetime.date(2020, 10, 1)
    oneday = datetime.timedelta(days=1)
    res = 0
    while start <= end:
        if start.day == 1 or start.weekday() == 0:  # 判断为周一或月初
            res += 2
        else:
            res += 1
        start += oneday  # 到下一天
    return res


print(run())
