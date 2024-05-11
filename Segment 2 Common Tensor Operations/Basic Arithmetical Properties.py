import numpy as np
import torch
import tensorflow as tf

print('******************pytorch operation*******************')
x_pt = torch.tensor([[10,20,30],
                     [30,50,60],
                     [10,90,80]])

print(x_pt)

print('****************addition by 2 *********************')

print(x_pt+2)

print('****************numpy operation*********************')
x_np= np.array([[10,20,30],
                [30,50,60],
                [10,90,80]])
print(x_np)

print('****************addition by 2 *********************')
print(x_np+2)

print('****************tensor operation*********************')
x_tf= tf.Variable([[10,20,30],
                [30,50,60],
                [10,90,80]])
print(x_tf)

print('****************addition by 2 *********************')
print(x_tf+2)

print('****************multiple by 2 *********************')
print(x_tf*2)