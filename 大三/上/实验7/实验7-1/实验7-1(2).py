import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")    # 标题
plt.xlabel("x axis caption")    # x坐标轴
plt.ylabel("y axis caption")    # y坐标轴
plt.plot(x ,y)  # 画图
plt.show()  # 显示

plt.figure(1)
x = np.linspace(0, 1 ,1000)
plt.subplot(2, 1, 1)
plt.title('y=x^2 & y=x')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 1)
plt.xlim(0, 1)
plt.xticks([0, 0.3, 0.6, 1])
plt.yticks([0, 0.5, 1])
plt.plot(x, x ** 2)
plt.plot(x, x)
plt.legend(['y=x^2', 'y=x'])
plt.savefig('1.png')
plt.show()

x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号"-"显示异常
plt.title("sin函数")
plt.plot(x, y)
plt.savefig('2.png')
plt.show()
