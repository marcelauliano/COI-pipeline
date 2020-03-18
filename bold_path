input=['marcela uliano\n', 'marcia uliano2\n', 'elisa\n', 'ana\n', 'claria matia\n']
for f in input:
    split=f.rstrip('\n').split(" ")
    if len(split) !=2:
        continue
    genus=split[0]
    species=split[1]
    if species: 
         print("wget http://v3.boldsystems.org/index.php/API_Public/sequence?taxon=" + genus + "%20" + species + "&marker=COI-5P" + "\n")
    else:
         print("wget http://v3.boldsystems.org/index.php/API_Public/sequence?taxon=" + genus + "&marker=COI-5P" + "\n")
