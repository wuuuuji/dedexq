import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

def drawbar(x,y,title,xlable,ylable):
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
    plt.title(title)    # 设置题目
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.xticks(rotation=45)
    plt.bar(x,y)
    plt.show()
    plt.savefig(title)

def drawline(x,y,x2,y2,title,xlable,ylable):
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
    plt.plot(x, y, 'r*--')
    plt.plot(x2, y2, 'b*--')
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.xticks(rotation=45)
    plt.bar(x, y)
    plt.show()
    plt.savefig(title)
engine = create_engine('mysql+pymysql://root:Qwe1355wu*.*@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1', con=engine)
print(detail.info)
print(detail.columns)
# 统计销售前十菜品并图表显示
y=detail.groupby('dishes_name').agg({'counts':'sum'}).sort_values('counts').tail(12)
# groupby()分组，基于行操作的
# agg()使用指定axis上的一个或多个进行聚合。
# tail()函数——返回最后n行。默认n=5
y=y[:-2]
# 删除最后两行
