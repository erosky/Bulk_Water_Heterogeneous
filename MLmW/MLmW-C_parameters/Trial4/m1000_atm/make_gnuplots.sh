#!/bin/bash

# Verify that system is equilibrated by looking for 
# stable potential evergy and mean square displacement
# Step Temp Press Volume TotEng KinEng PotEng c_1[4] 

mkdir eq_check

start=152
end=5152
logfile="./log.eq_MLC_T4_1000atm_245K"
directory="./eq_check"
datafile="./eq_check/graphite_ML_1000atm_e.dat"

temp="245"
pres="m1000atm"
T=245




# Convert timestep to ns, convert energies from kcal/mol to kJ/mol
sed "s/^[ \t]*//" ${logfile} | awk -v start=${start} -v end=${end} '{if ((NR>start)&&(NR<end)) { print $1/100000, $2, $3, $4, $5*4.184, $6*4.184, $7*4.184, $8 }}' > ${datafile}


# Plot and save Pot Energy
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/PE_${pres}.png'; \
            set title 'Potential Energy - nve, Sim ${temp}K'; \
            set ylabel 'kJ/mol'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:7"


# Plot and save Total Energy
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/E_${pres}.png'; \
            set title 'Total Energy - nve, Sim ${temp}K'; \
            set ylabel 'kJ/mol'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:5"


# Plot and save Mean square disp
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/MSD_${pres}.png'; \
            set title 'Mean Square Displacement vs Time - nve, Sim ${temp}K'; \
            set ylabel 'Angstroms'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:8"


# Plot and save Volume
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/VOL_${pres}.png'; \
            set title 'Box Volume - nve, Sim ${temp}K'; \
            set ylabel 'Cubic Angstroms'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:4"


# Plot and save Pressure
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/PRES_${pres}.png'; \
            set title 'Pressure - nve, Sim ${temp}K'; \
            set ylabel 'Pressure (atm)'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:3"

# Plot and save Temp
gnuplot -e "set terminal png size 1000,600; \
            set output '${directory}/TEMP_${pres}.png'; \
            set title 'Temperature - nve, Sim ${temp}K'; \
            set ylabel 'Temp (K)'; \
            set xlabel 'Time (ns)'; \
            set style data lines; \
            plot '${datafile}' using 1:2"

