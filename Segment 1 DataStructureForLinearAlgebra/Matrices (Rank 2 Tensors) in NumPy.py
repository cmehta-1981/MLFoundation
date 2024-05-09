import numpy as np

X = np.array([[25, 2],
              [5, 26],
              [3, 7]])
print(X)
print(X.shape)  # (3, 2) ,  3 rows 2 columns
print(X.size)  # 6 ,  total elements in metrix

print('# Select left column of matrix X (zero-indexed)')

print(X[:, 0])

print('# Select first row of matrix X (zero-indexed)')
print(X[0,:])

print('# Select 2nd  row of matrix X (zero-indexed)')
print(X[1,:])

print('# Select 3rd row of matrix X (zero-indexed)')
print(X[2,:])

# Select middle row of matrix X:
print(X[1,:])
print(X[1,:1])
print(X[0:1,0:1])