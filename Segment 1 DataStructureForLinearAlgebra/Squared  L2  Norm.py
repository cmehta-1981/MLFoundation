import numpy as np
import torch

x_np = np.array([10, 20, 30])

x_sqr = (10 ** 2 + 20 ** 2 + 30 ** 2)
print(x_sqr)  # 1400

# another way to do that by using dot

x_dot = np.dot(x_np, x_np)
print(x_dot)  # 1400

print("************************Max Norm**********************")

np_max = np.max([np.abs(10),np.abs(20),np.abs(30)])
print(np_max)
