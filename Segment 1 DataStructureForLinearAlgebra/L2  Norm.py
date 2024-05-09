import numpy as np
import torch
import tensorflow as tf

x_np = np.array([10, 20, 30])
x_sqrroot = (10 ** 2 + 20 ** 2 + 30 ** 2) ** (1 / 2)  # sum of squire of each element & squire root of the sum
print(x_sqrroot)  # 37.416573867739416

# another way to do that

x_sqr = np.linalg.norm(x_np)
print(x_sqr)  # 37.416573867739416
