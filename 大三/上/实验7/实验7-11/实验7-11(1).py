import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import pprint


titanic = pd.read_csv("./data/train.csv")   # 读取文件
titanic.head(5)     # 取文件前5行
titanic.info()      # 显示大概信息
print('\n\n')
print(titanic.describe())       # 生成描述性统计数据
print('\n\n')
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())     # 用年龄的中位数填充Na值
print(titanic.describe())       # 生成描述性统计数据
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0        # 性别男换成0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1      # 性别女换成1
print(titanic.loc[:5, 'Sex'])   # 打印性别0~5行的值,共6行
print(titanic["Embarked"].unique())     # 打印登船港口点的唯一值
print('\n\n')
titanic["Embarked"] = titanic["Embarked"].fillna('S')       # 登船港口点的空值换成"S"
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0     # 登船港口点"S"换成0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1     # 登船港口点"C"换成1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2     # 登船港口点"Q"换成2

predictors = ['Survived', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Sex', 'Pclass']
train_df = titanic[predictors]      # 划分数据
train_np = train_df.values      # 只取数值
y = train_np[:, 0].astype('int')    # 转换类型
X = train_np[:, 1:]
clf = LogisticRegression(max_iter=10000)
clf.fit(X, y)

data_test = pd.read_csv('./data/test.csv')
print(data_test.describe())
data_test['Age'] = data_test['Age'].fillna(data_test['Age'].median())
data_test.loc[data_test["Sex"] == "male", "Sex"] = 0        # 性别男换成0
data_test.loc[data_test["Sex"] == "female", "Sex"] = 1      # 性别女换成1\
data_test["Embarked"] =  data_test["Embarked"].fillna('S')
data_test.loc[data_test["Embarked"] == "S", "Embarked"] = 0     # 登船港口点"S"换成0
data_test.loc[data_test["Embarked"] == "C", "Embarked"] = 1     # 登船港口点"C"换成1
data_test.loc[data_test["Embarked"] == "Q", "Embarked"] = 2     # 登船港口点"Q"换成2
data_test["Fare"] = data_test["Fare"].fillna(data_test["Fare"].median())
test_df = data_test[['Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Sex', 'Pclass']]

test_np = test_df.values
test_x = test_np[:, 1:]
predicted_up = clf.predict(test_np)
print(predicted_up)
result = pd.DataFrame({'PassengerId': data_test['PassengerId'].values, 'Survived': predicted_up.astype(np.int32)})
result.to_csv('predictions.csv', index=False)