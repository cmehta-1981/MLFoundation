import torch
import numpy as np
X_pt = torch.tensor([[25, 2,10], [5, 26,10], [3, 7,10]])
print(X_pt)

print(X_pt.shape)
print(X_pt.size)

print(X_pt[1,:]) # N.B.: Python is zero-indexed; written algebra is one-indexed
