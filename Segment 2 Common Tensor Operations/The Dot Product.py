"""
If we have two vectors (say, x and y) with the same length n, we can calculate the dot product between them. This is
annotated several different ways, including the following: x⋅y xTy ⟨x,y⟩ Regardless which notation you use (I prefer 
the first), the calculation is the same; we calculate products in an element-wise fashion and then sum reductively 
across the products to a scalar value. That is, x⋅y=∑ni=1xiyi The dot product is ubiquitous in deep learning: It is 
performed at every artificial neuron in a deep neural network, which may be made up of millions (or orders of 
magnitude more) of these neurons.
"""

import numpy as np
import tensorflow as tf
import torch

print("**************************numpy operations***************")

x_np = np.array([10, 20, 30])

y_np = np.array([2, 3, 4])

print(" multiple of two tensors element wise ")
z_product = 10 * 2 + 20 * 3 + 30 * 4
print(z_product)  # output =  200

print(" by using dot product")
z_np = np.dot(x_np,y_np)
print(z_np) # output =  200

print("**************************pytorch operations***************")

x_pt = torch.tensor([10,20,30])
y_pt = torch.tensor([2,3,4])

z_pt = np.dot(x_pt,y_pt)
print(z_pt)     # output =  200
