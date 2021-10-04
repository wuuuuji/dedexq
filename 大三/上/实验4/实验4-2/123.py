# meal_order_detail1餐饮数据分析
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Qwe1355wu*.*@127.0.0.1:3306/testdb?charset=utf8')
# 1. 将数据集存入一个名为chipo的数据框内
detail=pd.read_sql_table('meal_order_detail1',con=engine)
# 2. 查看前10行内容
detail.head(10)
# 3. 数据集中有多少个列(columns)？
detail.shape[1]
# 4. 打印出全部的列名称
detail.columns
# 5. 数据集的索引是怎样的？
detail.index
# 6. 被下单数最多菜品(item)是什么?
detail.groupby('dishes_name').agg({'counts':'sum'}).idxmax()
# 7. 在item_name这一列中，一共有多少种商品被下单？
detail['dishes_name'].nunique()
# 8. 一共有多少个商品被下单？
detail['dishes_name'].unique()
# 9. 增加amounts_1列，将菜品价格改为￥金额,
detail['amounts_1']='$'+detail['amounts'].astype('str')
# 10.在该数据集对应的时期内，收入(revenue)是多少？
detail['revenue']=detail['amounts']*detail['counts']
# 11.在该数据集对应的时期内，一共有多少订单？
detail['order_id'].nunique()
# 12.每一单(order)对应的平均总价是多少？
detail['revenue'].sum() / detail['order_id'].nunique()