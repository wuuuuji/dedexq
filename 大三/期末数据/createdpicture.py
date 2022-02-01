import pandas as pd
from pyecharts import options
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from datetime import datetime

data = pd.read_excel("双色球中奖信息.xlsx")
blue_series = data.iloc[:, 3]  # 读取全部蓝球
red_series = data.iloc[:, 2]  # 读取全部红球
periods_series = data.iloc[:, 0]  # 读取全部期号

# 创建统计字典
blue_dict = dict.fromkeys(({i for i in range(1, 17)}), 0)  # 创建蓝球字典
red_dict = dict.fromkeys(({i for i in range(1, 34)}), 0)  # 创建红球字典
for b in blue_series:
    blue_dict[b] += 1  # 统计每个蓝球的编号出现的数量
for r1 in red_series:
    tem = r1.split()  # 读取红球series，将其转化为列表
    for r2 in tem:
        red_dict[int(r2)] += 1  # 统计每个红球的编号出现的次数


# 获取当前时间
tim = datetime.now().strftime('%Y-%m-%d')

# 柱状图
bar = Bar(init_opts=options.InitOpts(theme=ThemeType.MACARONS))
bar.add_xaxis(list(red_dict.keys()))
bar.add_yaxis('红球', list(red_dict.values()))
bar.add_yaxis('蓝球', list(blue_dict.values()))
bar.set_global_opts(title_opts=options.TitleOpts(title="最近{}期双色球红蓝球中奖次数".format(sum(blue_dict.values())), subtitle=tim))
bar.render('双色球(柱状图).html')
print("已生成双色球(柱状图)")

#  折线图
line = (
    Line(init_opts=options.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(list(red_dict.keys()))
        .add_yaxis('红球', list(red_dict.values()))
        .add_yaxis('蓝球', list(blue_dict.values()))
        .set_global_opts(title_opts=options.TitleOpts(title="最近{}期双色球折线图".format(sum(blue_dict.values())),
                                                      subtitle=tim,
                                                      ))
        )
line.render('双色球(折线图).html')
print("已生成双色球(折线图)")
