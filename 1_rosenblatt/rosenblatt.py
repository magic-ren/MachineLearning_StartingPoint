import dataset
from matplotlib import pyplot as plt  # matplotlib绘图开源软件，pyplot模块包含了很多绘图函数

xs, ys = dataset.get_beans(100)
print(xs)
print(ys)

# 配置图像
plt.title("Size-Toxicity Function")  # 设置图像名称
plt.xlabel("Bean Size")  # 设置横坐标的名字
plt.ylabel("Toxicity")  # 设置纵坐标的名字

# 这是使用rosenblatt模型调整w后的样子
w = 0.5
for i in range(100):  # 多重复几次，这样最后结果就是拟合的了
    for i in range(100):  # 以每个数据点为材料，一个个的用rosenblatt模型算法对w做调整
        x = xs[i]
        y = ys[i]
        y_pre = w * x  # 算出预测值
        e = y - y_pre  # 算出误差
        alpha = 0.05  # 学习率
        w = w + alpha * e * x  # e,小了就增加，大了就减小；x，解决了负数的问题；alpha，使得每次调整的步幅可控

y_pre = w * xs  # 可以直接乘以数组，最后得到数组
plt.plot(xs, y_pre)  # 绘制直线

plt.scatter(xs, ys)  # 绘制散点图
plt.show()
