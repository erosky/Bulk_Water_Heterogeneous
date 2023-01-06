import numpy as np
from scipy import constants

## command line to remove first to rows of output files:
# for f in ./*.xyz; do sed -i '1,2d' $f; done


s_top = 25+10.062
s_bot = 25

d_min = 3.2
d_max = 6.9


(liq_N, liq_V) = (0, 0)
(ice_N, ice_V) = (0, 0)


for r in np.arange(1,31):
	
	for i in np.arange(0,1000+250,250):
	#for i in [0]:
		
		data_file = f"MLmW_1atm/liquid/liquid_{r}_{i}.xyz"
		data = np.loadtxt(data_file)
		data = data[2:]
		data = np.transpose(data)
		x = data[0]
		y = data[1]
		z = data[2]
		v = data[3]
		
		for j,z_pos in enumerate(z):
			if (z_pos >= s_top):
				d = z_pos - s_top
			if (z_pos <= s_bot):
				d = s_bot - z_pos
			if ((d <= d_max) and (d >= d_min)):
				liq_N = liq_N+1
				liq_V = liq_V + v[j]
	
for r in np.arange(1,31):
	
	for i in np.arange(7000,8000+250,250):
	#for i in [8000]:
		
		data_file = f"MLmW_1atm/ice/ice_{r}_{i}.xyz"
		data = np.loadtxt(data_file)
		data = data[2:]
		data = np.transpose(data)
		x = data[0]
		y = data[1]
		z = data[2]
		v = data[3]
		
		for j,z_pos in enumerate(z):
			if (z_pos >= s_top):
				d = z_pos - s_top
			if (z_pos <= s_bot):
				d = s_bot - z_pos
			if ((d <= d_max) and (d >= d_min)):
				ice_N = ice_N+1
				ice_V = ice_V + v[j]

print (liq_N, liq_V, ice_N, ice_V)


#conversion to cm^3 mol^(−1)

# current data is N/A^3

def convert(N, V):
	mol = N/constants.N_A
	cm_cubed = V*((1/(1e8))**3)
	cm_per_mol = cm_cubed/mol
	return (cm_per_mol)
	
liq_v = convert(2230, 86576)
ice_v = convert(2230, 90324)

print (liq_v-ice_v)


