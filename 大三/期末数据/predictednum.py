import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# 读取数据
data = pd.read_excel("双色球中奖信息.xlsx")
blue_series = data.iloc[:, 3]  # 读取全部蓝球
red_series = data.iloc[:, 2]  # 读取全部红球


# 将每列球号码读出，写入到csv文件中，一共n行数据，对应n期数据
def readcsv(n, csv_name):

    red_num = []
    blue_num = []
    if 0 < n < 7:
        for rnum in red_series:
            tem = list(rnum.split())  # 读取红球series，将其转化为列表
            tem.sort()
            red_num.append(tem[n - 1])
            renum2 = pd.DataFrame(red_num)
            renum2.to_csv(csv_name, header=None)
    elif n == 7:
        for bnum in blue_series:
            blue_num.append(bnum)
            renum2 = pd.DataFrame(blue_num)
            renum2.to_csv(csv_name, header=None)
    fp = open(csv_name)
    s = fp.read()
    fp.close()
    a = s.split('\n')
    a.insert(0, 'numid,number')
    s = '\n'.join(a)
    fp = open(csv_name, 'w')
    fp.write(s)
    fp.close()


print("=="*20)
readcsv(1, 'rednum1.csv')
print("成功生成第一个红球CSV文件")
readcsv(2, 'rednum2.csv')
print("成功生成第二个红球CSV文件")
readcsv(3, 'rednum3.csv')
print("成功生成第三个红球CSV文件")
readcsv(4, 'rednum4.csv')
print("成功生成第四个红球CSV文件")
readcsv(5, 'rednum5.csv')
print("成功生成第五个红球CSV文件")
readcsv(6, 'rednum6.csv')
print("成功生成第六个红球CSV文件")
readcsv(7, 'bluenum.csv')
print("成功生成蓝球CSV文件")
print("=="*20)

# 获取数据，X_parameter为numid数据,Y_parameter为number数据
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['numid'], data['number']):
        X_parameter.append([int(single_square_feet)])
        Y_parameter.append(int(single_price_value))
    return X_parameter, Y_parameter

# 用Sklearn自带的LinearRegression回归，并将结果取整
def linearmodel(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    lml = linear_model.LinearRegression()
    lml.fit(X_parameters, Y_parameters)
    predict_outcome = int(lml.predict(predict_value)+0.5)
    predictions = {}
    predictions['截距'] = lml.intercept_
    predictions['斜率'] = lml.coef_
    predictions['预测值'] = predict_outcome
    return predictions

# 获取预测结果函数
def predicted_num(inputfile, num):
    X, Y = get_data(inputfile)
    predictvalue = 1000
    predictvalue = np.array(predictvalue).reshape(1, -1)
    result = linearmodel(X, Y, predictvalue)
    print(str(num)+'号球' + " 截距为：", result['截距'])
    print(str(num)+'号球' + " 斜率为：", result['斜率'])
    print(str(num)+'号球' + " 下期号码为: ", result['预测值'])


#  调用函数分别预测红球、蓝球
predicted_num('rednum1.csv', 1)
predicted_num('rednum2.csv', 2)
predicted_num('rednum3.csv', 3)
predicted_num('rednum4.csv', 4)
predicted_num('rednum5.csv', 5)
predicted_num('rednum6.csv', 6)
predicted_num('bluenum.csv', 7)
