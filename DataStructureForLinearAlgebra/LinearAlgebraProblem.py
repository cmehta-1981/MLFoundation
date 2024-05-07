# Question:
"""
    Sheriff has 180 km /h
    Bank Robber has 150 Km/h & 5 min ahead start from Sheriff
    How long does take Sheriff to cacth the robber
    What distance they travel at that point?
    For simplicity lets ignore traffic & acceleration etc.
"""

import numpy as np
import matplotlib.pyplot as plt

timeTaken = np.linspace(0, 40, 1000) # start, finish, n points
# distance travelling by robber 2.5 km/m means 2.5*timeTaken
dis_robber = 2.5 * timeTaken
print(dis_robber)
# distance travelling by Sheriff 3 km/m means 3*(timeTaken-5)
dis_sheriff = 3 * (timeTaken-5)
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('time (in minutes)')
plt.ylabel('distance (in km)')
xplot = ax.set_xlim([0, 40])
print(xplot)
ax.set_ylim([0, 100])
ax.plot(timeTaken, dis_robber, c='green')
ax.plot(timeTaken, dis_sheriff, c='brown')
plt.axvline(x=30, color='purple', linestyle='--')
_ = plt.axhline(y=75, color='purple', linestyle='--')


