import pandas as pd;
import numpy as np;
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Qwe1355wu*.*@127.0.0.1:3306/testdb?charset=utf8')
chipo = pd.read_sql_table('meal_order_detail1', con=engine)
