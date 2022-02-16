#!/bin/bash


cd ~/Freezing_Simulations/Bulk_Water_Heterogeneous/mW/500_atm/

for VARIABLE in 0 1 2 3 4
do
	echo $VARIABLE
	mkdir run_$VARIABLE
	sed -i -E "8 s/[0-9]+/$RANDOM/" in.bulk_min-eq-sim
	sed -i -E "9 s/[0-9]+/$VARIABLE/" in.bulk_min-eq-sim
	sed -i -E "10 s/[0-9]+/$VARIABLE/" in.bulk_min-eq-sim

	mpirun --use-hwthread-cpus ~/LAMMPS_Source/lammps/src/lmp_mpi -in in.bulk_min-eq-sim
done

