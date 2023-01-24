import numpy as np
from scipy import constants

## command line to remove first to rows of output files:
# for f in ./*.xyz; do sed -i '1,2d' $f; done

# Data output format
z_low, z_high, z_center, liquid density, liquid molar volume, molar volume difference


s_top = 25+10.062
s_bot = 25

d_min = 3.2
d_max = 6.9


z_bins = np.arange(0, 60+0.5, 0.5)


# conversion to cm^3 mol^(−1)
# current data is N/A^3

def convert(N, V):
	mol = N/constants.N_A
	cm_cubed = V*(1e-24)
	cm_per_mol = cm_cubed/mol
	return (cm_per_mol)


## Test sum of entire box
liq_sum = 0
ice_sum = 0
liq_N_runs = 0
ice_N_runs = 0


for r in np.arange(0,800+200,200):
	liq_N_runs = liq_N_runs + 1

	(liq_N, liq_V) = (0, 0)
	
	data_file = f"mW_1atm/liquid/liquid_{r}.xyz"
	data = np.loadtxt(data_file)
	data = data[2:]
	data = np.transpose(data)
	x = data[0]
	y = data[1]
	z = data[2]
	v = data[3]
	
	for i,z_pos in enumerate(z):
		if (z_pos >= s_top):
			d = z_pos - s_top
		if (z_pos <= s_bot):
			d = s_bot - z_pos
		if ((d <= d_max) and (d >= d_min)):
			liq_N = liq_N+1
			liq_V = liq_V + v[i]
	
	r_mol_volume = convert(liq_N, liq_V)
	liq_sum = liq_sum + r_mol_volume
	


for r in np.arange(5000,6000+250,250):
	ice_N_runs = ice_N_runs + 1
	
	(ice_N, ice_V) = (0, 0)
	
	data_file = f"mW_1atm/ice/ice_{r}.xyz"
	data = np.loadtxt(data_file)
	data = data[2:]
	data = np.transpose(data)
	x = data[0]
	y = data[1]
	z = data[2]
	v = data[3]
	
	for i,z_pos in enumerate(z):
		if (z_pos >= s_top):
			d = z_pos - s_top
		if (z_pos <= s_bot):
			d = s_bot - z_pos
		if ((d <= d_max) and (d >= d_min)):
			ice_N = ice_N+1
			ice_V = ice_V + v[i]
			
	r_mol_volume = convert(ice_N, ice_V)
	ice_sum = ice_sum + r_mol_volume


liq_v = liq_sum/liq_N_runs
ice_v = ice_sum/ice_N_runs

print (liq_v, ice_v, liq_v-ice_v)



