# 批量梯度下降算法 BatchGradientDescent

# 1、绘制w=0.1时的散点图和预测曲线
# 2、单次训练：
#    1）随意定义一个w=0.1
#    2）根据第2部分课程里的图4的全部样点的总体的代价函数，求得当前w的斜率，公式是2aw+b
#    3）定义学习率α=0.01
#    4）w=w-α*斜率
#    5）清空窗口、重新绘制散点图和预测曲线、暂停0.01秒
# 3、做1000次训练



import numpy as np
from matplotlib import pyplot as plt
import dataset

xs, ys = dataset.get_beans(100)
ys_pre = 0.1 * xs

plt.title("before train")
plt.xlabel("size")
plt.ylabel("toxicity")

plt.scatter(xs, ys)
plt.plot(xs, ys_pre)
plt.show()

w = 0.1
# 导数公式是2aw+b,再依据第2部分课程里的图4的全部样点的总体的代价函数
a = (1 / 100) * np.sum(xs ** 2)
b = (1 / 100) * np.sum((-2) * xs * ys)

for i in range(1000):
    k = 2 * a * w + b
    alpha = 0.01
    w -= alpha * k
    # plt.clf()  # 清空当前图表
    # plt.scatter(xs, ys)
    # ys_pre = w * xs
    # plt.xlim(0, 1)  # 将x轴的坐标固定
    # plt.ylim(0, 1.2)  # 将y轴的坐标固定
    # plt.plot(xs, ys_pre)
    # plt.pause(0.01)  # 暂停0.01

# 在命令行中运行就不会出现不断的弹新图表的问题了，因为matplotlib中绘制图形有阻塞、交互两种模式，命令行中执行是交互模式。

# 直接绘制结果
plt.scatter(xs, ys)
ys_pre = w * xs
plt.plot(xs, ys_pre)
plt.show()
