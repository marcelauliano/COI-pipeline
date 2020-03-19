#!/bin/bash

software="/software/team311/mu2/coi"
new_species="ectemnius_lituratus" #replace this with species name. Ex: homo_sapiens
python $software/get_bold.py -s $new_species -o out #python script that generates a wget line for coi-5p of the species present in the variable new_species 
sh out #execute the wget line to download coi-5p sequences
echo "all done"
done
