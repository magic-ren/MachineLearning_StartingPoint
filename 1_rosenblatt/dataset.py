import numpy as np  # 数学计算的库


# 获取原始数据集
def get_beans(counts):
    xs = np.random.rand(counts)
    xs = np.sort(xs)
    ys = [1.2 * x + np.random.rand() / 10 for x in xs]
    return xs, ys
