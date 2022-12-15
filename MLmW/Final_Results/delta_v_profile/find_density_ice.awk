#!/usr/bin/awk -f

# desired output:
# TIMESTEP, TIME, TEMP, ICE_RATIO, TOP_SA, BOTTOM_SA, TOTAL_SA

# TOTAL is the number of atoms in simulation, must remain constant throughout sim
# threshold is the order parameter threshold between ice and liquid

# sim timestep is 10 fs each step, 0.000001 ns
# ZTOP_UPPER
# ZTOP_LOWER
# ZBOTTOM_UPPER
# ZBOTTOM_LOWER
# YBIN_WIDTH = 3
# Angstroms

# Output one file for every 40,000 timesteps
# Outut file will have YBIN, N, XMIN, XMAX, XWIDTH, BIN_VOLUME, BIN_DENSITY



BEGIN { STEP = 8000000 ;
	TOTAL = 1794 ; 
	ZBIN = 55 ;
	ZBIN_WIDTH = 5.0 ;
	N = 0 ; VOL = ZBIN_WIDTH*49.22*49.01963593 ; start = 0 } 
NR>26830853 {
	if ($2=="TIMESTEP") {
		if (start==1) { print ZBIN "\t" N "\t" N/VOL ; exit } ; 
		start = 0 ; t = 1 ; a = 0
	}
	if (t==1 && $0==STEP) { step = $0 ; t = 0 ; start = 1 ; next }
  	if ($2=="ATOMS" && start==1) {
		a = 1 ; next
	}
	if (a==1 && $2==1) {
		# select z-bin
		if ($5>=ZBIN-ZBIN_WIDTH/2 && $5<ZBIN+ZBIN_WIDTH/2) {
			N = N+1 ;
		}
	}
}
#END {}
