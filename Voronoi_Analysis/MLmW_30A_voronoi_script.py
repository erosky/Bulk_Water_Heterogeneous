from ovito.io import *
from ovito.modifiers import *
from ovito.data import *
from ovito.pipeline import *
from ovito.io import export_file
import numpy as np


for r in np.arange(1,21):
	# Data import:
	pipeline = import_file(f'/data/emrosky-sim/Freezing_Simulations/Bulk_Water_Heterogeneous/MLmW/Ibeam-Width-Comparison/1_atm_30A/Constant_Cooling/run_{r}/prod.water.het_freeze_{r}-240-220.dump', multiple_frames = True)

	# Voronoi analysis:
	pipeline.modifiers.append(VoronoiAnalysisModifier())

	for i in np.arange(0,1000+250,250):
		export_file(pipeline, f"MLmW_1atm/30A_liquid/liquid_{r}_{i}.xyz", "xyz", frame=i,
		columns = ["Position.X", "Position.Y", "Position.Z", "Atomic Volume"])
    	
	for j in np.arange(7000,8000+250,250):
		export_file(pipeline, f"MLmW_1atm/30A_ice/ice_{r}_{j}.xyz", "xyz", frame=i,
		columns = ["Position.X", "Position.Y", "Position.Z", "Atomic Volume"])
    
