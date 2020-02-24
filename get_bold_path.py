import sys

#Giving a input wich is a text file containing a species name in each line (genus species), print a line that can be easily used to make a bold download of the COI-5P sequences

input = open(sys.argv[1]).readlines() 
output=open(sys.argv[2], "w")
for f in input:
    split=f.rstrip('\n').split(" ")
    if len(split) !=2:
        continue
    genus=split[0]
    species=split[1]
    if species: 
        output.write("wget http://v3.boldsystems.org/index.php/API_Public/sequence?taxon=" + genus + "%20" + species + "&marker=COI-5P" + "\n")
    else:
        output.write("wget http://v3.boldsystems.org/index.php/API_Public/sequence?taxon=" + genus + "&marker=COI-5P" + "\n")
output.close()
  
