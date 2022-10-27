#!/usr/bin/awk -f

# desired output:
# RUN TIMESTEP, NUMBER OF MOLECULES, DENSITY

BEGIN { STEP = 1000000 ; 
	RUN = 30 ;
	ZMAX_TOP = 55 ;
	ZMIN_TOP = 40 ;
	ZMAX_BOT = 20 ;
	ZMIN_BOT = 5 ;
	YDIM = 49.02 ;
	XDIM = 49.22 ;
	ZDIM = 30 ;
	VOL = ZDIM*XDIM*YDIM ;
	N = 0 ; start = 0 } 
{
	if ($2=="TIMESTEP") {
		if (start==1) { print RUN "\t" STEP "\t" N "\t" N/VOL ; exit } ; 
		start = 0 ; t = 1 ; a = 0
	}
	if (t==1 && $0==STEP) { step = $0 ; t = 0 ; start = 1 ; next }
  	if ($2=="ATOMS" && start==1) {
		a = 1 ; next
	}
	if (a==1 && $2==1) {
		# select z-bin and core
		if (($5>=ZMIN_TOP && $5<ZMAX_TOP) || ($5>=ZMIN_BOT && $5<ZMAX_BOT)) {
			N = N+1 ;
		}
	}
}
