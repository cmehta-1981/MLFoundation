"""
In the Substitution example, the two equations in the system are:
y=3x 
−5x+2y=2 

The second equation can be rearranged to isolate  y :
2y=2+5x 
y=2+5x2=1+5x2

solving the above two linear equation & finding the value of x & y
y = 3x -  First equation
-5x+2 *3x = 2 , replacing y vlue in 2nd equation
-5x +6x= 2
x= 2
then value of y  =  3*2 = 6

(x,y) = (2,6)

"""
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 1000)  # start, finish, n points
y1 = 3 * x
y2 = 1 + (5*x)/2

fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim([0, 3])
ax.set_ylim([0, 8])
ax.plot(x, y1, c='green')
ax.plot(x, y2, c='brown')
plt.axvline(x=2, color='purple', linestyle='--')
_ = plt.axhline(y=6, color='purple', linestyle='--')
