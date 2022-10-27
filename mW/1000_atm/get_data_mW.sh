#!/bin/bash
#
# extract data from dump files using the ice_ratio.awk, running_avg.ask, find_freezing_temp.py, and make_gnuplots.sh scripts

START=225
END=210
PRESSURE=-1000

for VARIABLE in 13 14 15 16 17 18 19 20
do
	echo $VARIABLE
	mkdir analysis/run_$VARIABLE

	./ice_ratio.awk run_$VARIABLE/prod.water.het_freeze_$VARIABLE-$START-$END.dump > analysis/run_$VARIABLE/ice_ratio.dat

	# make plot of ice ratio, raw data
	gnuplot -e "set terminal png size 1000,600; \
	    set output 'analysis/run_$VARIABLE/ice_ratio_raw.png'; \
            set title 'Ice Ratio vs. Temperature, mW, $PRESSURE atm - raw data'; \
            set ylabel 'N ice / N total'; \
            set xlabel 'Temp (K)'; \
            set style data lines; \
            set xrange [$START:$END] reverse; \
            set xtics $END,2; \
            plot 'analysis/run_$VARIABLE/ice_ratio.dat' using 3:7"
	
	# get running average of ice_ratio
	./running_avg.awk analysis/run_$VARIABLE/ice_ratio.dat > analysis/run_$VARIABLE/ice_ratio_smooth.dat

	# plot ice ratio
	python3 ~/Freezing_Simulations/Bulk_Water_Homogeneous/find_freezing_temp.py analysis/run_$VARIABLE/

	# plot data from log file
	./make_gnuplots.sh $VARIABLE
	

done


