#!/bin/bash

software="/software/team311/mu2/coi"
new_species="ectemnius_lituratus" #replace this with species name. Ex: homo_sapiens" 
concat="sequence?taxon=Ectemnius%20lituratus" #change here with the species name. Genus after taxon= and species after %20
python $software/get_bold.py -s $new_species -o out
echo "all done"
done
