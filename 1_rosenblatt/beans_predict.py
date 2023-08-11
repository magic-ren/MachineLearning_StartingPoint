import dataset
from matplotlib import pyplot as plt  # matplotlib绘图开源软件，pyplot模块包含了很多绘图函数

xs, ys = dataset.get_beans(100)
print(xs)
print(ys)

# 配置图像
plt.title("Size-Toxicity Function")  # 设置图像名称
plt.xlabel("Bean Size")  # 设置横坐标的名字
plt.ylabel("Toxicity")  # 设置纵坐标的名字

# 这是未使用rosenblatt模型调整w前的样子
# y=0.5*x
w = 0.5
y_pre = w * xs  # 可以直接乘以数组，最后得到数组。注意这里的数组是numpy里的数组，和python里的数组不一样。它有广播机制，可以让数组里的每个数字都乘以w，形成新数组。
plt.plot(xs, y_pre)  # 将所有的点连起来形成图形。这里形成的是直线。

plt.scatter(xs, ys)  # 绘制散点图
plt.show()
