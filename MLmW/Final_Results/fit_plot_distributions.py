#!/usr/bin/python
# 1 atm
# take list of runs as input
# ex.
# python3 plot_all_runs.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.optimize import curve_fit
import random


runs_1 = np.arange(1, 31, 1)
runs_500 = np.arange(1, 31, 1)
runs_1000 = np.arange(1, 31, 1)

limits_1 = [245, 220]
limits_500 = [245, 220]
limits_1000 = [245, 225]

bin_width = 1 # width of temperature bins

# create file for freezing temperatures in analysis folder
# data: RUN TEMP


# load data
data_dictionary_1 = {}
data_dictionary_500 = {}
data_dictionary_1000 = {}

freeze_temperatures_1 = []
freeze_temperatures_500 = []
freeze_temperatures_1000 = []

# curve fit information
def sigmoid(x, A, B, C, D):
	return A / (1.0 + np.exp(-B*(x-C))) - D

for run in runs_1:
	
	data_file = '1_atm/analysis/run_' + str(run) + '/ice_ratio_smooth.dat'
	data = np.loadtxt(data_file)
	data = np.transpose(data)

	# curve fit
	popt, pcov = curve_fit(sigmoid, data[1], data[2], p0=[0.55, 20, 230, 0.0])
	print (popt)
	print (pcov)
	fit = []
	for x in data[1]:
		fit.append(sigmoid(x, popt[0], popt[1], popt[2], popt[3]))
	gradient = np.gradient(fit)
	data = np.append(data, [gradient], axis=0)
	data = np.append(data, [fit], axis=0)
	data_dictionary_1[run] = data

	peak = np.argmax(gradient)
	freeze = data[1][peak]
	freeze_temperatures_1 = np.append(freeze_temperatures_1, freeze)

	# time = data[0]
	# temp = data[1]
	# ice = data[2]
	# gradient = data[3]


for run in runs_500:
	
	data_file = 'm500_atm/analysis/run_' + str(run) + '/ice_ratio_smooth.dat'
	data = np.loadtxt(data_file)
	data = np.transpose(data)
	
	# curve fit
	popt, pcov = curve_fit(sigmoid, data[1], data[2], p0=[0.55, 20, 235, 0.0])
	print (popt)
	print (pcov)
	fit = []
	for x in data[1]:
		fit.append(sigmoid(x, popt[0], popt[1], popt[2], popt[3]))
	gradient = np.gradient(fit)
	data = np.append(data, [gradient], axis=0)
	data = np.append(data, [fit], axis=0)
	data_dictionary_500[run] = data

	peak = np.argmax(gradient)
	freeze = data[1][peak]
	freeze_temperatures_500 = np.append(freeze_temperatures_500, freeze)


for run in runs_1000:
	
	data_file = 'm1000_atm/analysis/run_' + str(run) + '/ice_ratio_smooth.dat'
	data = np.loadtxt(data_file)
	data = np.transpose(data)
	
	# curve fit
	popt, pcov = curve_fit(sigmoid, data[1], data[2], p0=[0.55, 20, 240, 0.0])
	print (popt)
	print (pcov)
	fit = []
	for x in data[1]:
		fit.append(sigmoid(x, popt[0], popt[1], popt[2], popt[3]))
	gradient = np.gradient(fit)
	data = np.append(data, [gradient], axis=0)
	data = np.append(data, [fit], axis=0)
	data_dictionary_1000[run] = data

	peak = np.argmax(gradient)
	freeze = data[1][peak]
	freeze_temperatures_1000 = np.append(freeze_temperatures_1000, freeze)


# function for adding jitter to data points that overlap
def jitter():
	jit = random.uniform(-0.1, 0.1)
	return (jit)
	
# plot all trials on same plot, highlight freezing temperature
# calculate average freezing temperature and standard deviation
T_sum_1 = 0
S_sum_1 = 0

for T in freeze_temperatures_1:
	T_sum_1 = T_sum_1 + T
T_avg_1 = T_sum_1/len(freeze_temperatures_1)

for T in freeze_temperatures_1:
	S_sum_1 = S_sum_1 + (T - T_avg_1)**2
S_avg_1 = (S_sum_1/len(freeze_temperatures_1))**(0.5)



T_sum_500 = 0
S_sum_500 = 0

for T in freeze_temperatures_500:
	T_sum_500 = T_sum_500 + T
T_avg_500 = T_sum_500/len(freeze_temperatures_500)

for T in freeze_temperatures_500:
	S_sum_500 = S_sum_500 + (T - T_avg_500)**2
S_avg_500 = (S_sum_500/len(freeze_temperatures_500))**(0.5)


T_sum_1000 = 0
S_sum_1000 = 0

for T in freeze_temperatures_1000:
	T_sum_1000 = T_sum_1000 + T
T_avg_1000 = T_sum_1000/len(freeze_temperatures_1000)

for T in freeze_temperatures_1000:
	S_sum_1000 = S_sum_1000 + (T - T_avg_1000)**2
S_avg_1000 = (S_sum_1000/len(freeze_temperatures_1000))**(0.5)


# Fill temperature bins and fit a gaussian to data

temps_1 = range(limits_1[1], limits_1[0], bin_width)
temps_500 = range(limits_500[1], limits_500[0], bin_width)
temps_1000 = range(limits_1000[1], limits_1000[0], bin_width)

centers_1 = []
dist_1 = []
for N in range(len(temps_1)-1):
	center = temps_1[N] + 0.5*bin_width
	centers_1.append(center)
	N_freeze = 0
	for T in freeze_temperatures_1:
		if ((T>=temps_1[N])and(T<temps_1[N+1])):
			N_freeze = N_freeze+1
	dist_1.append(N_freeze)
	
centers_500 = []
dist_500 = []
for N in range(len(temps_500)-1):
	center = temps_500[N] + 0.5*bin_width
	centers_500.append(center)
	N_freeze = 0
	for T in freeze_temperatures_500:
		if ((T>=temps_500[N])and(T<temps_500[N+1])):
			N_freeze = N_freeze+1
	dist_500.append(N_freeze)
	
centers_1000 = []
dist_1000 = []
for N in range(len(temps_1000)-1):
	center = temps_1000[N] + 0.5*bin_width
	centers_1000.append(center)
	N_freeze = 0
	for T in freeze_temperatures_1000:
		if ((T>=temps_1000[N])and(T<temps_1000[N+1])):
			N_freeze = N_freeze+1
	dist_1000.append(N_freeze)



def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))
    


gaus_range = np.linspace(220, 240, 10000)

# create file for plot of all runs
all_runs_plot = 'ML_dist_npt_test.png'

custom_lines = [Line2D([0], [0], color='#000066', lw=4),
                Line2D([0], [0], color='#669900', lw=4),
                Line2D([0], [0], color='#cc99ff', lw=4)]

plt.figure(1, figsize=[8.4,4.8])
plt.xlim(245,220)
#plt.ylim(0,1.0)
plt.title('Heterogeneous Freezing Temp Distributions\nML-mW Model, Cooling rate 0.25K/ns')
plt.xlabel('Temperature (K)')
plt.ylabel('Number of Freezing events')
plt.legend(custom_lines, ['1 Atm', '-500 Atm', '-1000 Atm'], loc='lower right')

plt.bar(centers_1, dist_1, width=bin_width, color='#000066', edgecolor='#000066', alpha=0.6)
plt.bar(centers_500, dist_500, width=bin_width, color='#669900', edgecolor='#669900', alpha=0.6)
plt.bar(centers_1000, dist_1000, width=bin_width, color='#cc99ff', edgecolor='#cc99ff', alpha=0.6)

#plt.plot(gaus_range, gaussian(gaus_range, *popt1), label='fit', color='#000066')
#plt.plot(gaus_range, gaussian(gaus_range, *popt500), label='fit', color='#669900')
#plt.plot(gaus_range, gaussian(gaus_range, *popt1000), label='fit', color='#cc99ff')

plt.tight_layout()
plt.savefig(all_runs_plot, dpi=300)



