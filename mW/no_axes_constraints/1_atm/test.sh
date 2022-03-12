#!/bin/bash

# Find number of water molecules in run
N_WATER=$(sed -n '14'p run_0/log.eq_het_freeze_0 | tr -d -c 0-9)
echo $N_WATER
# edit ice_ratio.awk script to appropriate number of water molecules
sed -i -E "12 s/[0-9]+/$N_WATER/" ice_ratio.awk
