#!/bin/bash
#
# extract data from dump files using the ice_ratio.awk, running_avg.ask, find_freezing_temp.py, and make_gnuplots.sh scripts

START=225
END=210
PRESSURE=-1000

for VARIABLE in 1
do
	echo $VARIABLE
	mkdir analysis/test_$VARIABLE

	./ice_ratio.awk test_$VARIABLE/prod.het_freeze_test-$START-$END.dump > analysis/test_$VARIABLE/ice_ratio.dat

	# make plot of ice ratio, raw data
	gnuplot -e "set terminal png size 1000,600; \
	    set output 'analysis/test_$VARIABLE/ice_ratio_raw.png'; \
            set title 'Ice Ratio vs. Temperature, mW, $PRESSURE atm - raw data'; \
            set ylabel 'N ice / N total'; \
            set xlabel 'Temp (K)'; \
            set style data lines; \
            set xrange [$START:$END] reverse; \
            set xtics $END,2; \
            plot 'analysis/test_$VARIABLE/ice_ratio.dat' using 3:7"
	
	# get running average of ice_ratio
	./running_avg.awk analysis/test_$VARIABLE/ice_ratio.dat > analysis/test_$VARIABLE/ice_ratio_smooth.dat

	# plot ice ratio
	#python3 ~/Freezing_Simulations/Bulk_Water_Homogeneous/find_freezing_temp.py analysis/test_$VARIABLE/

	# plot data from log file
	#./make_gnuplots.sh $VARIABLE
	

done


