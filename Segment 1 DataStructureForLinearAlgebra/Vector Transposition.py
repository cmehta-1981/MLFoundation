import numpy as np
import tensorflow as tf
import torch

print('# Transposing a regular 1-D array has no effect...')

x_np = np.array([20,10,5])
print(x_np)
print(x_np.shape)
x_np = x_np.T
print(x_np)   # Transposing a regular 1-D array has no effect...
print(x_np.T.shape)

print('# ...but it does we use nested "matrix-style" brackets:')
y_np = np.array([[20,10,5]])
print(y_np)
print(y_np.shape)
print('transpose of tensor is : - \n',y_np.T)


