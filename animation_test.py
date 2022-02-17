import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

test_data = "mW/1_atm/analysis/test_1/ice_ratio.dat"

ice_ratio = pd.read_csv(test_data, sep='\t', header=None, names=['timestep','time (ns)','temperature (K)','ice', 'liquid', 'total', 'ice/total'])



fig, ax = plt.subplots()

ax.set_xlim(225, 205)
ax.set_ylim(0, 1)

init = ice_ratio.iloc[:int(1)] #select data range
x = init['temperature (K)']
y = init['ice/total']
line, = ax.plot(x, y)


def animate(i):
    data = ice_ratio.iloc[:int(i+1)] #select data range
    x = data['temperature (K)']
    y = data['ice/total']
    line.set_xdata(x)  # update the data.
    line.set_ydata(y)
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
