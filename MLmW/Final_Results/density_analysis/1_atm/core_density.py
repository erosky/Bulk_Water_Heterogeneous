import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

output = "core_density/core_density.dat"
data = np.loadtxt('core_density/timesteps.dat')
data = data.transpose()

avg_data = np.mean(data, axis=1)
std_data = np.std(data, axis=1)

f = open(output, 'w')
f.write("avg density (#/A^3): \t" + str(avg_data[3]) + "\n")
f.write("std density (#/A^3): \t" + str(std_data[3]) + "\n")
f.write("avg #: \t" + str(avg_data[2]) + "\n")
f.write("std #: \t" + str(std_data[2]))

