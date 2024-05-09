import numpy as np
import torch
import tensorflow as tf

x_np = np.array([[10,20,30],
                 [40,50,60],
                 [10,20,70]])
print(x_np)

print(' ***********************# transpose metrix***************')

print(x_np.T)

print(' ***********************# Pytorch operation***************')
x_pt = torch.tensor([[10,20,30],
                    [40,50,60],
                    [10,20,70]])
print(x_pt)

print(' ***********************# transpose metrix***************')
print(x_pt.T)

print(' ***********************# Tensorflow operation***************')
x_tf = tf.Variable([[10,20,30],
                    [40,50,60],
                    [10,20,70]])
print(x_tf)

print(' ***********************# transpose metrix***************')
print(tf.transpose(x_tf))