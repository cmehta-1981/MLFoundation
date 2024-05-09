import numpy as np
import tensorflow as tf
import torch

# type argument is optional, e.g.: dtype=np.float16

# In summary, dtype=np.float16 is useful when memory efficiency is critical, but you should be aware of its limited
# precision compared to other floating-point types

x_np = np.array([25, 2, 5], dtype=np.int16)
print(x_np)

print(len(x_np))  # 3
print(x_np.size)  # 3
print(x_np.shape)  # (3,)
print(x_np[0])  # 25
print(type(x_np))
print(type(x_np[0]))


