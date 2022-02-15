#!/usr/bin/awk -f

# desired output:
# TIMESTEP, TIME, TEMP, R1_DENSITY, R2_DENSITY, .....

# Command to run script:
# ./density_profile.awk run_X/dumfile.dump > analysis/run_X/density_profile.dat

# Best to add header to the density_profile.dat file before running the above command

# slices is the number of slices along z-axis where density is measured
# TOTAL is the number of atoms in simulation, must remain constant throughout sim
# threshold is the order parameter threshold between ice and liquid

# sim timestep is 10 fs each step, 0.000001 ns

# Script:
# 1. determine box bounds at each timestep
# 2. divide box z-axis into N number of slices
# 3. for timestep, compute the number of atoms in each slice
# 4. divide by the volume of each slice to get number density (D)
# 5. convert to molar volume -> 0.6022/D
# 6. Append values into row in the correct order


BEGIN { TOTAL = 4096 ; threshold = 0.54 ; ice = 0 ; start = 0 ; slice = 10} 
{
	if ($2=="TIMESTEP") {
		if (start==1) { 
			print step "\t" step*0.00001 "\t" 215-step*0.25*0.00001 "\t" ice "\t" TOTAL-ice "\t" TOTAL "\t" ice/TOTAL
		} ; 
		t = 1 ; a = 0 ; next 
	}
	if (t==1) { step = $0 ; t = 0 ; start = 1 ; next }
  if ($2=="ATOMS") {
		a = 1 ; ice = 0 ; water = 0 ; next
	}
	if (a==1 && $10>threshold) { ice++ }
}
END { print step "\t" step*0.00001 "\t" 215-step*0.25*0.00001 "\t" ice "\t" TOTAL-ice "\t" TOTAL "\t" ice/TOTAL }
