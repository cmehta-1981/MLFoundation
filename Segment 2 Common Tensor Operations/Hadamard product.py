"""
If two tensors have the same size, operations are often by default applied element-wise. This is not matrix multiplication, 
which we'll cover later, but is rather called the Hadamard product or simply the element-wise product.
The mathematical notation is  A⊙X
"""

import  numpy as np
import torch
import tensorflow as tf

x_np = np.array([[10,20,30],
                [30,50,60],
                [10,90,80]])
print(x_np)
print(' ***************adding by 2 *************** of tensors x_np')
y_np = x_np+2
print(y_np)

print(' ***************addition of two tensors *************')

z_np = x_np+y_np
print(z_np)

print(' ***************multiple of two tensors *************')

z_np = x_np*y_np
print(z_np)