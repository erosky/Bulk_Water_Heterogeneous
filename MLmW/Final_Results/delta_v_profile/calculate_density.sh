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

for RUN in 1 2 3 4 5
do
	echo $RUN
	mkdir 1_atm/liquid/run_$RUN
	#for timestep in 0
	for timestep in {0..50000..5000}
	do
		output=1_atm/liquid/run_$RUN/$timestep.dat
		truncate -s 0 $output
		sed -i -E "22 s/[0-9]+/$timestep/" find_density.awk
		for zbin in {30..55..1}
		do
			sed -i -E "24 s/([0-9]+\.?[0-9]*)|([0-9]*\.[0-9]+)/$zbin/" find_density.awk
			./find_density.awk $DIR/run_$RUN/prod.water.het_freeze_$RUN-240-220.dump >> $output
		done
	done
done

