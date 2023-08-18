# 固定步长梯度下降算法

# 1、绘制w=0.1时的散点图和预测曲线
# 2、在单个样本点上操作：
#    1）随意定义一个w=0.1
#    2）知道单个点的代价函数，此函数的求导函数是2aw+b,所以就是2*x^2*w-2*x*y
#    3）定义固定步长step=0.01
#    4）如果斜率是负数，那么w就要增加w=w+step；如果斜率是正数，那么w就要减少w=w-step
#    5）清空窗口、重新绘制散点图和预测曲线、暂停0.01秒
# 3、在每个样本上都做一次
# 4、在全部样本上训练100次


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
step = 0.01
for _ in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        k = 2 * (x ** 2) * w - 2 * x * y
        if k < 0:
            w += step
        elif k > 0:
            w -= step
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
