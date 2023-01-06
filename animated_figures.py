import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg


test_data = "MLmW/Final_Results/m1000_atm/analysis/run_1/ice_ratio.dat"

ice_ratio = pd.read_csv(test_data, sep='\t', header=None, names=['timestep','time (ns)','temperature (K)','ice', 'liquid', 'total', 'ice/total'])

print(ice_ratio.head())


############################################################
# Animated plot of ice ratio data
############################################################

fig1, ax1 = plt.subplots()

ax1.set_xlim(248, 233)
ax1.set_ylim(0, 1)

init = ice_ratio.iloc[:int(1)] #select data range
x = init['temperature (K)']
y = init['ice/total']
line, = ax1.plot(x, y)


def animate(i):
    data = ice_ratio.iloc[:int(i+1)] #select data range
    x = data['temperature (K)']
    y = data['ice/total']
    line.set_xdata(x)  # update the data.
    line.set_ydata(y)
    return line,

frames=np.arange(0, 6000, 50)

temps={}
T_current = 248
for n in frames:
    T = 248 - 0.0025*n
    if (T_current - T > 1):
    	T_current = round(T)
    temps[n] = T_current
    
print (temps)


ani = animation.FuncAnimation(
    fig1, animate, frames, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

#plt.show()



############################################################
# Animated plot of simulation
############################################################

mov0 = "MLmW/Final_Results/m1000_atm/analysis/run_1/animation_frames"
mov1 = "MLmW/Final_Results/m1000_atm/analysis/run_2/animation_frames"
mov2 = "MLmW/Final_Results/m1000_atm/analysis/run_3/animation_frames"
mov3 = "MLmW/Final_Results/m1000_atm/analysis/run_4/animation_frames"
mov4 = "MLmW/Final_Results/m1000_atm/analysis/run_5/animation_frames"
mov5 = "MLmW/Final_Results/m1000_atm/analysis/run_6/animation_frames"
mov6 = "MLmW/Final_Results/m1000_atm/analysis/run_7/animation_frames"

mov0_frames = {}
mov1_frames = {}
mov2_frames = {}
mov3_frames = {}
mov4_frames = {}
mov5_frames = {}
mov6_frames = {}


for n in frames:
    filename = mov0+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov0_frames[n]=img

for n in frames:
    filename = mov1+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov1_frames[n]=img
    
for n in frames:
    filename = mov2+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov2_frames[n]=img

for n in frames:
    filename = mov3+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov3_frames[n]=img
    
for n in frames:
    filename = mov4+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov4_frames[n]=img

for n in frames:
    filename = mov5+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov5_frames[n]=img
    
for n in frames:
    filename = mov6+'/MLmW_1000atm_%s.png' % f"{n:04}"
    #print(filename)
    img = mpimg.imread(filename)
    mov6_frames[n]=img


''' 
mov, ax = plt.subplots()
ax.imshow(mov_frames[0])
    
ims = []
for i in frames:
    im = ax.imshow(mov_frames[i], animated=True)
    if i == 0:
        ax.imshow(mov_frames[i])  # show an initial one first
    ims.append([im])

ani = animation.ArtistAnimation(mov, ims, interval=10, blit=True,
                                repeat_delay=1000)

ani.save("animation_vid.mp4")

'''

############################################################
# Multuple animations plots together with temperature
############################################################

# plot movie and data together!

######################
# VERTICAL ORIENTATION
######################
'''
fig2 = plt.figure(figsize=(2.0, 4.0), frameon=False)
#fig2, ax = plt.subplots(4, 2, figsize=(5, 5))
#fig2.tight_layout()

temp_ax = fig2.add_subplot(4, 2, 1, aspect='equal')
ax0 = fig2.add_subplot(4, 2, 2, aspect='equal')
ax1 = fig2.add_subplot(4, 2, 3, aspect='equal')
ax2 = fig2.add_subplot(4, 2, 4, aspect='equal')
ax3 = fig2.add_subplot(4, 2, 5, aspect='equal')
ax4 = fig2.add_subplot(4, 2, 6, aspect='equal')
ax5 = fig2.add_subplot(4, 2, 7, aspect='equal')
ax6 = fig2.add_subplot(4, 2, 8, aspect='equal')
'''

######################
# HORIZONTAL ORIENTATION
######################
fig2 = plt.figure(figsize=(4.0, 2.0), frameon=False)
#fig2, ax = plt.subplots(4, 2, figsize=(5, 5))
#fig2.tight_layout()

temp_ax = fig2.add_subplot(2, 4, 1, aspect='equal')
ax0 = fig2.add_subplot(2, 4, 2, aspect='equal')
ax1 = fig2.add_subplot(2, 4, 3, aspect='equal')
ax2 = fig2.add_subplot(2, 4, 4, aspect='equal')
ax3 = fig2.add_subplot(2, 4, 5, aspect='equal')
ax4 = fig2.add_subplot(2, 4, 6, aspect='equal')
ax5 = fig2.add_subplot(2, 4, 7, aspect='equal')
ax6 = fig2.add_subplot(2, 4, 8, aspect='equal')



fig2.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.99, wspace=0.1, hspace=0.1)

temp_ax.set_xticks([]) 
temp_ax.set_yticks([]) 
temp_ax.axis('off')

temp = temp_ax.text(0.1, 0.2, '248 K', dict(size=20))
im0 = ax0.imshow(mov0_frames[0])
im1 = ax1.imshow(mov1_frames[0])
im2 = ax2.imshow(mov2_frames[0])
im3 = ax3.imshow(mov3_frames[0])
im4 = ax4.imshow(mov4_frames[0])
im5 = ax5.imshow(mov5_frames[0])
im6 = ax6.imshow(mov6_frames[0])

ax0.set_xticks([])
ax0.set_yticks([])
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])
ax3.set_xticks([])
ax3.set_yticks([])
ax4.set_xticks([])
ax4.set_yticks([])
ax5.set_xticks([])
ax5.set_yticks([])
ax6.set_xticks([])
ax6.set_yticks([])



def animate(i):
    temp_ax.clear()
    print(temps[i])
    temp = temp_ax.text(0.1, 0.2, '%s K' % temps[i], dict(size=20))
    temp_ax.set_xticks([]) 
    temp_ax.set_yticks([])
    temp_ax.axis('off') 
    im0.set_array(mov0_frames[i])
    im1.set_array(mov1_frames[i])
    im2.set_array(mov2_frames[i])
    im3.set_array(mov3_frames[i])
    im4.set_array(mov4_frames[i])
    im5.set_array(mov5_frames[i])
    im6.set_array(mov6_frames[i])
    return im0, im1, im2, im3, im4, im5, im6, temp,

ani = animation.FuncAnimation(fig2, animate, frames, interval=50, blit=True, save_count=50)

ani.save("freeze_dist_horizontal.mp4", dpi=500)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

#plt.show()



'''
# plot movie and data together as an inset!
%matplotlib notebook

#fig2, (ax1, ax2) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 2]})
fig3, ax = plt.subplots(figsize=(10,6))
      
ax.set_xlim(225, 205)
ax.set_ylim(0, 1)

init = ice_ratio.iloc[:int(1)] #select data range
x = init['temperature (K)']
y = init['ice/total']
line, = ax.plot(x, y)

inset = fig3.add_axes([0.55, 0.09, .4, .4])
inset.imshow(mov_frames[0])
plt.setp(inset, xticks=[], yticks=[])


def animate(i):
    inset.imshow(mov_frames[i])
    data = ice_ratio.iloc[:int(i+1)] #select data range
    x = data['temperature (K)']
    y = data['ice/total']
    line.set_xdata(x)  # update the data.
    line.set_ydata(y)
    return line,

ani = animation.FuncAnimation(fig3, animate, frames, interval=10, blit=True, save_count=50)

# To save the animation, use e.g.
#
ani.save("animation_test.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
'''

