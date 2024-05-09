import numpy as np
import torch

x_np = np.array([25,  2,  5])
x_abs = np.abs(25) + np.abs(2) + np.abs(5)
print(x_abs)
print(type(x_abs))
x_pt = torch.tensor(abs(25))+torch.tensor(abs(2))+torch.tensor(abs(5))
print(x_pt)