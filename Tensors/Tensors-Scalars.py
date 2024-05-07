import numpy as np
import torch
import tensorflow as tf

X = np.array([[10,20],
              [30,40],
              [50,60]])
print(X[1,:])
print(X.T)

y= torch.tensor([[10,20]])
print(y)

print(tf.__version__)

X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(X_tf)

print("**************************************************************")
Y = np.array([[42,4,7,99],
              [-99,-3,17,22]])
print(Y)

print(Y.T)

A = np.array([[25,10],
              [-2,1]])
B= np.array([[-1,7],
             [10,8]])

print(A*B)

A = torch.tensor([[25,10],
              [-2,1]])
B= torch.tensor([[-1,7],
             [10,8]])
print(A*B)

A = tf.Variable([[25,10],
              [-2,1]])
B= tf.Variable([[-1,7],
             [10,8]])

print(A*B)
print(A.dot(B))