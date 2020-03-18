import sys
import re

#Giving a input wich is a text file containing a species name in each line (genus species), print a line that can be easily used to make a bold download of the COI-5P sequences. This script will also edit the input file, it will produce a bold line only for the genus, if the species variable contains numbers or is empty.

#Usage: python get_bold_path.py <list.name.file> <bold_line>

input = open(sys.argv[1]).readlines() 
output=open(sys.argv[2], "w")
output2=open(sys.argv[3], "w")
for f in input:
        split=f.rstrip('\n').split(" ")
        if len(split) !=2:
                continue
        genus=split[0]
        species=split[1]
        m = re.search(r'\d$', species) 
        if m is not None:
                output2.write(genus + "\n")
                output.write("wget" + " " + genus + "%20"  + "&marker=COI-5P" + "\n")
        elif m is None:
                output2.write(genus + " " + species + "\n")
                output.write("wget" + " " + genus + "%20" + species + "&marker=COI-5P" + "\n")
        else:
                output2.write(genus + "\n")
                output.write("wget" + " " + genus + "%20"  + "&marker=COI-5P" + "\n")
output.close()
  
