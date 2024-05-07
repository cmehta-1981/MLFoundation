import numpy as np
import tensorflow as tf
import  torch

print("*************************** Numpy concepts ********************************* ")
x =  25.6
print(x)
print(type(x))
y = 30
print(y)
print(type(y))
np_sum =  x+y
print(np_sum)
print(type(np_sum))

'''
Scalars in PyTorch
PyTorch and TensorFlow are the two most popular automatic differentiation libraries (a focus of the Calculus I(https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/3-calculus-i.ipynb) and 
Calculus II(https://github.com/jonkrohn/ML-foundations/blob/master/notebooks/4-calculus-ii.ipynb) subjects in the ML Foundations series) in Python, 
itself the most popular programming language in ML.
PyTorch tensors are designed to be pythonic, i.e., to feel and behave like NumPy arrays.
The advantage of PyTorch tensors relative to NumPy arrays is that they easily be used for operations on GPU (see for more details (https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fpytorch.org%2Ftutorials%2Fbeginner%2Fexamples_tensor%2Ftwo_layer_net_tensor.html) for example).
Documentation on PyTorch tensors, including available data types, is here.(https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fpytorch.org%2Fdocs%2Fstable%2Ftensors.html)
'''
print("*************************** PyTorch concepts ********************************* ")
x_pt = torch.tensor(25)
print(x_pt)
y_pt = torch.tensor(30,dtype=torch.float16)
print(y_pt)
print(x_pt.shape)

'''
Scalars in TensorFlow (version 2.0 or later)
Tensors created with a wrapper, 
all of which you can read about here:(https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.tensorflow.org%2Fguide%2Ftensor)

tf.Variable
tf.constant
tf.placeholder
tf.SparseTensor
Most widely-used is tf.Variable, which we'll use here.

As with TF tensors, in PyTorch we can similarly perform operations, and we can easily convert to and from NumPy arrays.

Also, a full list of tensor data types is available here.(https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdtypes%2FDType)
'''
print("*************************** Tensorflow concepts ********************************* ")
x_tf = tf.Variable(25,dtype=tf.int16)
print(x_tf)
y_tf = tf.Variable(30,dtype=tf.int16)
print(y_tf)
z_tf = x_tf+y_tf
print(z_tf)
print(z_tf.shape)

# note that NumPy operations automatically convert tensors to NumPy arrays, and vice versa

print(z_tf.numpy())
print(type(z_tf.numpy()))

tf_float = tf.Variable(25., dtype=tf.float16)
print(tf_float)
