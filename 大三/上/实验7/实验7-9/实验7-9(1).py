from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split


def showdigists(image, labele):
    plt.figure(figsize=(12, 8))  # 绘画图窗大小(单位是英寸)
    for i in range(65):
        plt.subplot(9, 8, i + 1)  # 向当前图窗添加子图
        plt.imshow(image[i], cmap='gray')
        title = 'True:' + str(labele[i])
        plt.title(title)
        plt.axis('off')
    plt.show()


digits = datasets.load_digits()
showdigists(digits.images, digits.target)
X = digits.data / 255
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)
mlp_hw = MLPClassifier(solver='lbfgs',
                       hidden_layer_sizes=[100, 100],
                       activation='relu',
                       alpha=1e-5,
                       random_state=62)
# 使用数据训练神经网络模型
mlp_hw.fit(X_train, y_train)
print('\n\n\n')
print('代码运行结果')
print('=' * 25)
print()
print('测试数据集得分:{:.2f}%'.format(mlp_hw.score(X_test, y_test) * 100))
print()
print('=' * 25)
