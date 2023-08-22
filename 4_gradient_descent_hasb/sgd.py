# 以w为偏导数和b为偏导数共同作用进行随机梯度下降

import dataset
from matplotlib import pyplot as plt

xs, ys = dataset.get_beans(100)
plt.title("bean size_toxicity")
plt.xlabel("size")
plt.ylabel("toxicity")
plt.scatter(xs, ys)

w = 0.1
b = 0.1
ys_pre = w * xs + b
plt.plot(xs, ys_pre)

plt.show()

for _ in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        kw = 2 * (x ** 2) * w + (2 * x * b - 2 * x * y)  # 见图10
        kb = 2 * b + (2 * x * w - 2 * y)  # 见图11
        alpha = 0.01
        w -= alpha * kw
        b -= alpha * kb
    plt.clf()
    plt.scatter(xs,ys)
    ys_pre = w * xs + b
    plt.xlim(0,1)
    plt.ylim(0,1.2)
    plt.plot(xs, ys_pre)
    plt.pause(0.01)

# plt.scatter(xs, ys)
# ys_pre = w * xs + b
# plt.xlim(0, 1)
# plt.ylim(0, 1.2)
# plt.plot(xs, ys_pre)
# plt.show()
