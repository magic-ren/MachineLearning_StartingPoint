import dataset
import numpy as np
from matplotlib import pyplot as plt

# y=wx
# 1、绘制散列点和w=0.1时的直线（就是预测函数的直线）（plot1）
xs, ys = dataset.get_beans(100)

w = 0.1
ys_pre = w * xs

plt.title("beans_predict")
plt.xlabel("size")
plt.ylabel("toxicity")
plt.scatter(xs, ys)
plt.plot(xs, ys_pre)
plt.show()

# 2、计算出当w=0.1时均方误差的值
es = ys - ys_pre  # 这里类型是numpy的array，它们相减是将每个元素相减，最终得到一个相减后的数组。这个数组里存放的是每个点的误差。
es2 = es ** 2  # 两个乘号是平方的意思。最终得到的也是每个元素相乘后的数组。这个数组里存放的是每个点的误差的平方。
e = np.sum(es2) / 100  # numpy的sum方法是将数组里的每个数相加。这里的意思是将每个点的误差的平方相加，再除以样本数。也就是均方误差。
print(e)

# 3、计算出当w在[0.1,3)，步幅为0.1时的所有均方误差的值，并将这些(w,e)的点绘制出来（是一个开口向上的抛物线）（plot2）
ws = np.arange(0, 3, 0.1)  # 注意这里用的是numpy的arange方法，不是python的range方法
es = []
for w in ws:
    e = np.sum((ys - w * xs) ** 2) / 100
    es.append(e)  # 数组增加元素
plt.title("cost:w(0-2.9)")
plt.xlabel("w")
plt.ylabel("e")
plt.plot(ws, es)
plt.show()

# 4、计算出均方误差e最小时的w值（也就是开口向上的抛物线的顶点，公式见图4），然后将此w的预测函数和散列点都绘制出来（plot3）
w = np.sum(xs * ys) / np.sum(xs ** 2)
ys_pre = w * xs
plt.title("result")
plt.xlabel("size")
plt.ylabel("toxicity")
plt.scatter(xs, ys)
plt.plot(xs, ys_pre)
plt.show()
