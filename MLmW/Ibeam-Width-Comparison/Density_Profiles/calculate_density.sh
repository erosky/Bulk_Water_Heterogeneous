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

DIR=../1_atm_30A/


for timestep in {50000..150000..2000}
do
	output=1_atm_30A/$timestep.dat
	truncate -s 0 $output
	sed -i -E "22 s/[0-9]+/$timestep/" find_density.awk
	for zbin in {0..40..1}
	do
		sed -i -E "23 s/([0-9]+\.?[0-9]*)|([0-9]*\.[0-9]+)/$zbin/" find_density.awk
		./find_density.awk $DIR/eq.ML_graphite_1atm_240K.dump >> $output
	done
done

