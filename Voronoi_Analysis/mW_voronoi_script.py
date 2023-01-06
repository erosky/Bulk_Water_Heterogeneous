from ovito.io import *
from ovito.modifiers import *
from ovito.data import *
from ovito.pipeline import *
from ovito.io import export_file
import numpy as np


for r in np.arange(1,21):
	# Data import:
	pipeline = import_file(f'/data/emrosky-sim/Freezing_Simulations/Bulk_Water_Heterogeneous/mW/1_atm/run_{r}/prod.water.het_freeze_{r}-225-210.dump', multiple_frames = True)

	# Voronoi analysis:
	pipeline.modifiers.append(VoronoiAnalysisModifier())

	#for i in np.arange(0,1200,200):
	for i in [1200]:
		export_file(pipeline, f"mW_1atm/liquid/liquid_{i}.xyz", "xyz", frame=i,
		columns = ["Position.X", "Position.Y", "Position.Z", "Atomic Volume"])
    	
	#for j in np.arange(4000,6000,250):
	for j in [6000]:
		export_file(pipeline, f"mW_1atm/ice/ice_{j}.xyz", "xyz", frame=i,
		columns = ["Position.X", "Position.Y", "Position.Z", "Atomic Volume"])
    
