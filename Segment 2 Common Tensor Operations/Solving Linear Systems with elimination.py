'''
In the Elimination example, the two equations in the system are:
2x−3y=15
4x+10y=14

Both equations can be rearranged to isolate  y . Starting with the first equation:
−3y=15−2x
y=15−2x−3=−5+(2x/3)

Then for the second equation:
4x+10y=14
2x+5y=7
5y=7−2x
y=7−2x/5

(x,y) = (6,-1)

'''

import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 10000)  # start, finish, n points

y1 = -5 + (2*x)/3
y2 = (7-2*x)/5

fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')

# Add x and y axes:
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

ax.set_xlim([-2, 10])
ax.set_ylim([-6, 4])
ax.plot(x, y1, c='green')
ax.plot(x, y2, c='brown')
plt.axvline(x=6, color='purple', linestyle='--')
_ = plt.axhline(y=-1, color='purple', linestyle='--')
