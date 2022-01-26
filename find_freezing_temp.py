#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

N_args = len(sys.argv)
inputs = sys.argv
directory = inputs[1]

# load data
# plot all trials on same plot, highlight freezing temperature

#data = np.loadtxt('analysis/run_0/ice_ratio_smooth.dat')
data_file = directory + 'ice_ratio_smooth.dat'
data = np.loadtxt(data_file)
data = np.transpose(data)

time = data[0]
temp = data[1]
ice = data[2]

output1 = directory + 'ice_ratio.png'
gradient = np.gradient(ice)

plt.figure(1)
plt.plot(temp, ice)
plt.savefig(output1)

output3 = directory + 'ice_ratio.png'

plt.figure(1)
plt.plot(temp, gradient)
plt.savefig(output3)

peak = np.argmax(gradient)
print (temp[peak])


