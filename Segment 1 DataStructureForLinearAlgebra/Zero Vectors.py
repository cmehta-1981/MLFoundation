import numpy as np
import torch
import tensorflow as tf

z_np = np.zeros(3)
print(z_np)  # [0. 0. 0.]

z_pt = torch.zeros(3)
print(z_pt)  # tensor([0., 0., 0.])

z_tf = tf.Variable(0)
print(z_tf)
