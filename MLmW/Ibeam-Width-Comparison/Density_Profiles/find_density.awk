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



BEGIN { STEP = 150000 ; 
	ZBIN = 40 ;
	ZBIN_WIDTH = 1.0 ;
	N = 0 ; VOL = 2412.7465 ; start = 0 } 
{
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
		if ($5>=ZBIN && $5<ZBIN+ZBIN_WIDTH) {
			N = N+1 ;
		}
	}
}
#END {}
