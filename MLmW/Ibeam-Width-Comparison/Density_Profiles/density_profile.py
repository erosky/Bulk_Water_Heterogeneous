# plot and analyze total surface area
# interested to know, how variable the total surface area is over different timesteps

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

output = "m1000atm_24A_dens_profile.dat"

#timesteps = list(range(50000, 148000, 2000))
timesteps = list(range(26000, 48000, 2000))
zbin_edges = list(range(0, 36, 1))
print (zbin_edges)


## ybin columns are labels for data in each zbin dataframe
ybin_columns = ['ZBIN', 'N', 'ZBIN_VOLUME']

data = []
## Load the data structure outlined above
##

for step in timesteps:
	zbin_data = np.loadtxt('./m1000_atm_24A/'+str(step)+'.dat')
	zbin_data = zbin_data.transpose()
	data.append(zbin_data[2])


avg_data = np.mean(data, axis=0)
print(avg_data)	

f = open(output, 'w')
for bin in range(36):
	print (bin)
	f.write(str(zbin_edges[bin]) + '\t' + str(avg_data[bin]) + '\n')

##
##
'''
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




'''



