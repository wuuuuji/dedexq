import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Qwe1355wu*.*@127.0.0.1:3306/testdb?charset=utf8')
# 连接数据库
detail = pd.read_sql_table("meal_order_detail1", con=engine)
detailGroup = detail[['order_id', 'counts', 'amounts']].groupby(by='order_id')
print('分组后的订单详情表为:', detailGroup)
print('\n\n\n')

print('订单详情表分组后前五组的均值为:\n', detailGroup.mean().head())
print('\n\n\n')

print('订单详情表分组后前五组的标准差为:\n', detailGroup.std().head())
print('\n\n\n')

print('订单详情表分组后前五组的大小为:\n', detailGroup.size().head())
print('\n\n\n')

print('1 订单详情表的菜品销量与售价的和与均值为:\n', detail[['counts', 'amounts']].agg([np.sum, np.mean]))
print('\n\n\n')

print('2 订单详情表的菜品销量总和与售价的均值为:\n', detail.agg({'counts': np.sum, 'amounts': np.mean}))
print('\n\n\n')

print('3 菜品订单详情表的菜品销量总和与售价的总和与均值为:\n ', detail.agg({'counts': np.sum, 'amounts': [np.mean, np.sum]}))
print('\n\n\n')


def DoubleSum(data):
    s = data.sum() * 2
    return s


print('菜品订单详情表的菜品销量两倍总和为:\n', detail.agg({'counts': DoubleSum}, axis=0))
print('\n\n\n')


def DoubleSum1(data):
    s = np.sum(data) * 2
    return s


print('订单详情表的菜品销量两倍总和为:\n', detail.agg({'counts': DoubleSum1}, axis=0).head())
print('\n\n\n')

print('订单详情表的菜品销量与售价的和的两倍为:\n', detail[['counts', 'amounts']].agg(DoubleSum1))
print('\n\n\n')

print('订单详情表分组后前3组的均值为:\n', detailGroup.agg(np.mean).head(3))
print('\n\n\n')

print('订单详情表分组后前3组的标准差为:\n', detailGroup.agg(np.std).head(3))
print('\n\n\n')

print('订单详情表分组前3组每组菜品总数和售价均值为:\n', detailGroup.agg({'counts': np.sum, 'amounts': np.mean}).head(3))
print('\n\n\n')

print('订单详情表的菜品销量与售价的均值为:\n', detail[['counts', 'amounts']].apply(np.mean))
print('\n\n\n')

print('订单详情表分组后前3组的均值为:\n', detailGroup.apply(np.mean).head(3))
print('\n\n\n')

print('订单详情表分组后前3组的标准差为:\n', detailGroup.apply(np.std).head(3))
print('\n\n\n')

print('订单详情表的菜品销量与售价的两倍为:\n', detail[['counts', 'amounts']].transform(lambda x: x * 2).head(4))
print('\n\n\n')

detail = pd.read_sql_table('meal_order_detail1',con=engine)
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date']=[i.date() for i in detail['place_order_time']]
detailGroup = detail[['date','counts','amounts']].groupby(by='date')
print('订单详情表前5组每组的数目为:\n',detailGroup.size().head())
print('\n\n\n')
dayMean = detailGroup.agg({'amounts':np.mean})
print('订单详情表前5组每日菜品均价为:\n',dayMean.head())
print('\n\n\n')
dayMedian = detailGroup.agg({'amounts':np.median})
print('订单详情表前5组每日菜品售价中位数为:\n',dayMedian.head())
print('\n\n\n')
daySaleSum = detailGroup.apply(np.sum)['counts']
print('订单详情表前5组每日菜品售出数目为:\n',daySaleSum.head())