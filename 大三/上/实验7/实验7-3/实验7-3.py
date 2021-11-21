import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


def drawbar(x, y, title, xlable, ylable):
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
    plt.title(title)  # 设置题目
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.xticks(rotation=45)
    plt.bar(x, y)
    plt.show()
    plt.savefig(title)


def drawline(x, y, x2, y2, title, xlable, ylable, a, b):
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
    plt.plot(x, y, 'r*--')
    plt.plot(x2, y2, 'b*--')
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.xticks(rotation=45)
    plt.legend([a, b])
    plt.bar(x, y)
    plt.show()
    plt.savefig(title)


engine = create_engine('mysql+pymysql://root:Qwe1355wu*.*@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1', con=engine)
print(detail.info)
print(detail.columns)
# 统计销售前十菜品并图表显示
y = detail.groupby('dishes_name').agg({'counts': 'sum'}).sort_values('counts').tail(12)
# groupby()分组，基于行操作的
# agg()使用指定axis上的一个或多个进行聚合。
# tail()函数——返回最后n行。默认n=5
y = y[:-2]
# 删除最后两行
drawbar(y.index, y['counts'], '菜品销售', '菜品', '销售额')
detail['day'] = detail['place_order_time'].apply(lambda x: x.strftime('%Y-%m-%d'))
# strftime接收以时间元组，并返回以可读字符串表示的当地时间
y2 = detail.groupby('day').agg({'amounts': 'sum'})
drawbar(y2.index, y2['amounts'], '每天销售', '日期', '销售额')
# 统计凉拌波菜每天销售情况，及总销售菜品情况
y3 = detail[detail['dishes_name'] == '凉拌菠菜'].groupby('day').agg({'counts': 'sum'})
y4 = detail.groupby('day').agg({'counts': 'sum'})
drawline(y3.index, y3['counts'], y4.index, y4['counts'], '每天销售', '日期', '销售数量', "凉拌波菜销售情况", '总销售情况')
