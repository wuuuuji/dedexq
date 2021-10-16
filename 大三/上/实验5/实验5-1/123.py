# 招聘数据探索与分析
import pandas as pd
# 1. 读取数据并存为一个名叫job_info的数据框。
job_info = pd.read_csv('./data/job_info.csv', encoding='gbk', header=None)
# 2. 将列命名为：['公司', '岗位', '工作地点', '工资', '发布日期']。
job_info.columns=['公司', '岗位', '工作地点', '工资', '发布日期']
# 3. 哪个岗位招聘需求最多？
print("哪个岗位招聘需求最多？")
print(job_info['岗位'].value_counts())
# 4. 取出9月3日发布的招聘信息。
print("9月3日发布的招聘信息")
print(job_info['发布日期'].value_counts())
print(job_info[job_info['发布日期']=='09-03'])
print(job_info.loc[job_info['发布日期']=='09-03', :])
# 5. 找出工作地点在深圳的数据分析师招聘信息。
print(job_info['工作地点'].str[0:2]=='深圳')
index1=job_info[ '工作地点'].apply(lambda x:'深圳' in x)
index2=job_info['岗位']=='数据分析师'
res1=job_info.loc[index2&index1,:]