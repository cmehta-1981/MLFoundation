import numpy as np

'''
1. x & y are orthogonal vectors if xTy = 0 , T = Transpose
2. Are at 90  degree angle to each other (Assuming non zero norms )
3. n-dimensional space has max n-mutually orthogonal vectors (assuming non zero norms)
4. Orthonormal vectors are orthonormal and all have unit norms 
    e.i. basic vectors are an examples (i = (1,0) , j= (0,1)

'''

x_np = np.array([1, 0])
y_np = np.array([0, 1])

z_np = np.dot(x_np, y_np)
print(z_np)  # output =  0
