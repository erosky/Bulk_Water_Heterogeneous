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


BEGIN { YBIN = 77.751 ;
	STEP = 0 ;
	TOTAL = 1794 ; 
	ZBIN = 30.957 ;
	ZBIN_WIDTH = 2.985 ;
	YBIN_WIDTH = 3.11004 ; N = 0 ; XMIN = 9999 ; XMAX = -9999 ; start = 0 } 
{
	if ($2=="TIMESTEP") {
		if (start==1) { print YBIN "\t" N "\t" XMIN "\t" XMAX "\t" XMAX-XMIN "\t" (XMAX-XMIN)*YBIN_WIDTH*ZBIN_WIDTH "\t" N/((XMAX-XMIN)*YBIN_WIDTH*ZBIN_WIDTH) ; exit } ; 
		start = 0 ; t = 1 ; a = 0 
	}
	if (t==1 && $0==STEP) { step = $0 ; t = 0 ; start = 1 ; next }
  	if ($2=="ATOMS" && start==1) {
		a = 1 ; next
	}
	if (a==1 && $2==2) {
		# select z-bin
		if ($5>=ZBIN && $5<ZBIN+ZBIN_WIDTH) {
			# select y-bin
			if ($4>=YBIN && $4<YBIN+YBIN_WIDTH) {
				N = N+1 ;
				if ($3<XMIN) { XMIN = $3 } ;
				if ($3>XMAX) { XMAX = $3 } ;	
			}
		}
	}
}
#END {}
