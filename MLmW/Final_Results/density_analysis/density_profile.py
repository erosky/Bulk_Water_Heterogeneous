# plot and analyze total surface area
# interested to know, how variable the total surface area is over different timesteps

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd


N_total = 2126 # Total number of water molecules

## Timesteps is a list of timesteps, each associated with a dictionary of zbin slices. These are the keys to timestep_dict
timesteps = [0, 320000, 640000]
#steps = list(range(0, 640000, 80000))
timestep_dict = {}
## The items in timestep_dict are  zbin_data_dict

## zbin_edges is a list of the zbin edge values, these are the keys tp each zbin_data_dict, and the keys to time_avg_dict
zbin_edges = [10.062, 13.047, 16.032, 19.017, 22.002, 24.987, 27.972, 30.957]
## The items in  zbin_data_dict are numpy arrays


## ybin columns are labels for data in each zbin dataframe
ybin_columns = ['YBIN', 'N', 'XMIN', 'XMAX', 'XWIDTH', "YBIN_VOLUME", "YBIN_DENSITY"]


## Load the data structure outlined above
##
for step in timesteps:
	zbin_data_dict = {}
	timestep_dict[step] = zbin_data_dict
	for zbin_file in os.listdir('Eight_Layer/run_5/'+str(step)):
		zbin = zbin_file[:-4]
		print (zbin)
		zbin_data = np.loadtxt('Eight_Layer/run_5/'+str(step)+'/'+zbin_file)
		zbin_data_dict[float(zbin)] = zbin_data
##
##

## Average over every timestep to profuce a new data structure. The new data structure is a dictionary of time averaged zbin_data
## zbin_edges are the keys to time_avg_dict
time_avg_dict = {}

# Theres gonna be a dictionary with eight keys, each array inside each key must be averaged over the other timesteps

for zbin in zbin_edges:
	zbin_dict = {}
	time_avg_dict[zbin] = zbin_dict
	zbin_arrays = []
	for step in timesteps:
		zbin_arrays.append(timestep_dict[step][zbin])
	time_avg_data = np.average(zbin_arrays, axis=0)
	zbin_dict['dataframe'] = pd.DataFrame(time_avg_data, columns=ybin_columns)



## Now we will sum over the y-slices to add to the zbin_dict dictionaries
density_data = []
width_data = []
fraction_data = []

for zbin in zbin_edges:
	dataset = time_avg_dict[zbin]
	df = dataset['dataframe']
	N = df['N'].sum()
	V = df['YBIN_VOLUME'].sum()
	zbin_density = N/V
	avg_density = df['YBIN_DENSITY'].mean()
	avg_width = df['XWIDTH'].mean()
	# write data
	time_avg_dict[zbin]['N'] = N
	time_avg_dict[zbin]['density'] = zbin_density
	density_data.append(zbin_density)
	time_avg_dict[zbin]['avg_density'] = avg_density
	time_avg_dict[zbin]['fraction'] = N/N_total
	fraction_data.append(N/N_total)
	time_avg_dict[zbin]['width'] = avg_width
	width_data.append(avg_width)


print(time_avg_dict)
## zbin keys are the per z slice data options available in each z layer. They are the keys to each zbin_data_dict.
zbin_keys = ['dataframe', 'density', 'N', 'fraction', 'width']


## Plot the results
plt.figure(1)
plt.plot(zbin_edges, density_data)
plt.show()








