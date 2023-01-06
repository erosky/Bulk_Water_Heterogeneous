#! /bin/bash

python3 voronoi_script.py

for f in ./MLmW_1atm/liquid/*.xyz; do sed -i '1,2d' $f; done
for f in ./MLmW_1atm/ice/*.xyz; do sed -i '1,2d' $f; done
