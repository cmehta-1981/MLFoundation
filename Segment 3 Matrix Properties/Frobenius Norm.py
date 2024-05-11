import numpy as np
import torch
import tensorflow as tf

x_np = np.array([[1, 2], [3, 4]])

Frobenius_Norm = (1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2) ** (1 / 2)
print(Frobenius_Norm)  # output  = 5.477225575051661

Frobenius_Norm = np.linalg.norm(x_np)  # same function as for vector L2 norm
print(Frobenius_Norm)  # output  = 5.477225575051661

X_pt = torch.tensor([[1, 2], [3, 4.]])  # torch.norm() supports floats only
Frobenius_Norm = torch.norm(X_pt)
print(Frobenius_Norm)  # output  = tensor(5.4772)

X_tf = tf.Variable([[1, 2], [3, 4.]]) # tf.norm() also supports floats only
Frobenius_Norm = tf.norm(X_tf)
print(Frobenius_Norm)  # output  = Tensor(5.477226)