# 绘制以w为自变量的包含b的代价函数（一个曲面）


import dataset
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 绘制3维图形的工具

fig = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)
ax.set_zlim(0, 2)
ax.set_xlabel("w")
ax.set_ylabel("e")
ax.set_zlabel("b")
xs, ys = dataset.get_beans(100)

bs = np.arange(-2, 2, 0.1)
ws = np.arange(-2, 2, 0.1)
for b in bs:
    es = []
    for w in ws:
        ys_pre = w * xs + b
        e = 0.01 * np.sum((ys - ys_pre) ** 2)
        es.append(e)
    ax.plot(ws, es, b, zdir='y')  # 见图12
plt.show()
