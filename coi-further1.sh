#!bin/bash
software="/software/team311/mu2/coi"
database="/lustre/scratch116/vr/projects/vgp/user/mu2/coi-db/coi.updated.fa" #latest database for now
fasta="$1"
fasta_prefix=${fasta#*2020/}
database_prefix=${database#*coi-db/}

#Step 1: replace variable new_species with the scientific name of the species you want to include COI-5P sequences for in the blast database.
new_species="$2" #Replace this with species name underscored. Ex: homo_sapiens.


if [ "$1" == "-h" ]; then
  echo "Usage: $1 fasta sequence to be analyzed, $2 species name ex: homo_sapiens"
  exit 0
fi


if [ -z $1 ]; then
        echo "fasta sequence not provided"
        exit 1
else
        echo "fasta file is $fasta"
fi


if [ -z $2 ]; then
        echo "No new species to include in the blast db? This must be wrong"
        exit 1
else
        echo "New species included is $new_species"
fi
python $software/get_bold.py -s $new_species -o out #python script that generates a wget line for coi-5p of the species present in the variable new_specie 
sh out

if [[ -f ./newseqs ]]
then
        echo "newseqs created. Editing and adding it to blast db"
else
        echo "no newseqs created"
        exit 1
fi
