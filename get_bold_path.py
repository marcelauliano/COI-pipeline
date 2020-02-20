import sys
input = open(sys.argv[1]).readlines() 
output=open(sys.argv[2], "w")
for f in input:
  split=f.rstrip('\n').split(" ")
   genus=split[0]
   species=split[1]
   output.write("wget http://v3.boldsystems.org/index.php/API_Public/sequence?taxon=" + genus + "%20" + species + "&marker=COI-5P" + "\n")
output.close()
