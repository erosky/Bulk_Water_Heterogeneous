#!/usr/bin/python
# 1 atm
# take list of runs as input
# ex.
# python3 plot_all_runs.py 0 1 2 3 4 5 6

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N_args = len(sys.argv)
inputs = sys.argv
runs = inputs[1:]


# create file for freezing temperatures in analysis folder
# data: RUN TEMP
data_file = 'analysis/freeze_data.dat'
f = open(data_file, "w")


# load data
data_dictionary = {}
freeze_temperatures = []
freeze_data = []

# curve fit information
def sigmoid(x, A, B, C, D):
	return A / (1.0 + np.exp(-B*(x-C))) - D

for run in runs:
	
	data_file = 'analysis/run_' + run + '/ice_ratio_smooth.dat'
	data = np.loadtxt(data_file)
	data = np.transpose(data)

	# curve fit
	popt, pcov = curve_fit(sigmoid, data[1], data[2], p0=[0.6, 20, 202, 0.0])
	print (popt)
	print (pcov)
	fit = []
	for x in data[1]:
		fit.append(sigmoid(x, popt[0], popt[1], popt[2], popt[3]))
	gradient = np.gradient(fit)
	data = np.append(data, [gradient], axis=0)
	data = np.append(data, [fit], axis=0)
	data_dictionary[run] = data

	peak = np.argmax(gradient)
	grad_pk = max(gradient)
	start = 0
	thresh = 0.0001
	for i,value in enumerate(gradient):
		if (start==0 and value>thresh):
			freeze_start = data[0][i] #time of nucleation starting
			temp_start = data[1][i] #temp when nucleation starts
			start=1
		if (start==1 and value<=thresh):
			freeze_end = data[0][i]
			temp_end = data[1][i]
			start=0
	
	freeze = data[1][peak]
	fraction = fit[-1]
	freeze_temperatures = np.append(freeze_temperatures, freeze)
	f.write(run + '\t' + str(freeze) + '\t' + str(grad_pk) + '\t' + str(fraction) + '\t' + str(freeze_start) + '\t' + str(freeze_end) + '\t' + str(temp_start) + '\t' + str(temp_end) + '\n')

	# time = data[0]
	# temp = data[1]
	# ice = data[2]
	# gradient = data[3]

# close data file
f.close()




