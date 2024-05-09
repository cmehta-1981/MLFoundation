import tensorflow as tf

X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(X_tf)

images_tf = tf.zeros([32, 28, 28, 3])
print(images_tf)