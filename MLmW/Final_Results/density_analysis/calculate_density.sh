#!/bin/bash
#
# Calculate average surface area of carbon-water interface prior to freezing
# Input dump file
# Output a data file with the following:
# YBIN, N, XMIN, XMAX, BIN_VOLUME, BIN_DENSITY

# For each z-bin we want to know the average density
# -- for each z-bin, find the average densiy averaged over y-bin
# -- where the y-bin density is N_in_bin / bin_volume 
# -- where bin_volume = (max_x - min_x)*y_binw*z_binw
# -- the average density in that z-layer is the average density of all y-bins

DIR=../1_atm/


for RUN in 5
do
	echo $RUN
	mkdir 1_atm/run_$RUN
	for timestep in 0
	#for timestep in {0..1920000..320000}
	do
		mkdir Eight_Layer/run_$RUN/$timestep
		sed -i -E "22 s/[0-9]+/$timestep/" find_density.awk
		for zbin in 10.062 13.047 16.032 19.017 22.002 24.987 27.972 30.957
		do
			sed -i -E "24 s/([0-9]+\.?[0-9]*)|([0-9]*\.[0-9]+)/$zbin/" find_density.awk
			for ybin in 0.0 3.11004 6.22008 9.33012 12.44016 15.5502 18.66024 21.77028 24.88032 \
			27.99036 31.1004 34.21044 37.32048 40.43052 43.54056 46.6506 49.76064 52.87068 55.98072 \
			59.09076 62.2008 65.31084 68.42088 71.53092 74.64096 77.751
			do
				sed -i -E "21 s/([0-9]+\.?[0-9]*)|([0-9]*\.[0-9]+)/$ybin/" find_density.awk
				./find_density.awk $DIR/Constant_Cooling/run_$RUN/prod.ibeam_cooling_$RUN.dump >> ./Eight_Layer/run_$RUN/$timestep/$zbin.dat
			done
		done
	done
done

