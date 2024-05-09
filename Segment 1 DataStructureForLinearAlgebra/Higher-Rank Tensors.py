import tensorflow as tf
import torch

'''
Higher-Rank Tensors
As an example, rank 4 tensors are common for images, where each dimension corresponds to:

Number of images in training batch, e.g., 32
Image height in pixels, e.g., 28 for MNIST digits
Image width in pixels, e.g., 28
Number of color channels, e.g., 3 for full-color images (RGB)
'''
image_tf = tf.zeros([32,28,28,3])
print(image_tf)

print('*********************************************************************************************')

image_pt = torch.zeros([32,28,28,3])
print(image_pt)