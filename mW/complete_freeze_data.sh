#! /bin/bash
# output data structure:
# Run freezeTemp freezeSlope iceFraction freezeStartTime freezeEndTime freezeStartTemp freezeEndTemp startVol endVol dVol startPres endPres dPres preFreezeMSD
# units:
# time - ns, temp - K, Vol - cubic angstrom, Pres - atm, preFreezeMSD - square angstroms per unit time

DIR=$(pwd)

# Check for correct number of input arguments
if [ $# -lt 2 ]
then
  echo
  echo "  requires freeze_data_v2.dat file"
  echo "  Usage: $0 runs"
  echo "   e.g.: $0 0 1 2 3 4"
  echo
  exit ${E_ARGS}
fi

RUNS=${@: 1}
echo $RUNS

datafile="./analysis/complete_freeze_data_v2.dat"
window=4.0 #4 ns
skip=100

for VAR in $RUNS
do
	DATA=$(awk -v run=${VAR} '{if ($1==run) { print $0 }}' ./analysis/freeze_data_v2.dat)
	st=$(echo $DATA | awk '{print $5}')
	st_lo=$(bc -l <<<"${st}-${window}")
	end=$(echo $DATA | awk '{print $6}')
	end_hi=$(bc -l <<<"${end}+${window}")
	
	volume=$(cat ./analysis/run_${VAR}/run_homog_freeze_${VAR}.dat | awk -v skip=${skip} -v st=${st} -v st_lo=${st_lo} -v end=${end} -v end_hi=${end_hi} 'BEGIN { N_st = 0 ; N_end = 0 ; V_st = 0 ; V_end = 1 } {if ((NR % skip == 0) && ($1 > st_lo) && ($1 < st)) {N_st = N_st + 1 ; V_st = V_st + $4 } if ((NR % skip == 0) && ($1 > end) && ($1 < end_hi)) { N_end = N_end + 1 ; V_end = V_end + $4 }} END { print V_st/N_st "\t" V_end/N_end "\t" (V_st/N_st - V_end/N_end) }')
	
	pressure=$(cat ./analysis/run_${VAR}/run_homog_freeze_${VAR}.dat | awk -v skip=${skip} -v st=${st} -v st_lo=${st_lo} -v end=${end} -v end_hi=${end_hi} 'BEGIN { N_st = 0 ; N_end = 0 ; P_st = 0 ; P_end = 1 } {if ((NR % skip == 0) && ($1 > st_lo) && ($1 < st)) {N_st = N_st + 1 ; P_st = P_st + $3 } if ((NR % skip == 0) && ($1 > end) && ($1 < end_hi)) { N_end = N_end + 1 ; P_end = P_end + $3 }} END { print P_st/N_st "\t" P_end/N_end "\t" (P_st/N_st - P_end/N_end) }')
	
	MSD=$(cat ./analysis/run_${VAR}/run_homog_freeze_${VAR}.dat | awk -v st=${st} -v st_lo=${st_lo} -v end=${end} -v end_hi=${end_hi} 'BEGIN { MSD_lo = 0 ; MSD_hi = 1 ; T_lo = 9999 ; T_hi = 0 } {if (($1 < T_lo) && ($1 > st_lo) && ($1 < st)) {MSD_lo = $8 ; T_lo = $1 ; next } if (( $1 > T_hi) && ($1 > end) && ($1 < end_hi)) { MSD_hi = $8 ; T_hi = $1 ; next }} END { print (MSD_hi - MSD_lo)/(T_hi - T_lo) }')
	
	
	echo $DATA $volume $pressure $MSD >> ${datafile}
done



