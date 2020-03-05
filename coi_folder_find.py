#Marcela Uliano-Silva

from datetime import date
import os
import argparse
today= date.today()
parser= argparse.ArgumentParser(add_help=False)
parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help= "This script was written to deal with the Sanger Tola assembly team folder structure. It searches for a folder called 'coi' from the path given as first argument '-p'. Arguments are described as follows") 
parser.add_argument("-p", help= "-p is root path directory to look for 'coi' folder in subsequent directories", required = "True")
parser.add_argument("-output1", help= "output1 is a file that presents a list of directories that contain a folder 'coi'", required = "True")
parser.add_argument("-output2", help= "output1 is a file that presents a list of directories that DOES NOT contain a folder 'coi'", required = "True")
args = parser.parse_args()
output1=open(args.output1, "w")
output2=open(args.output2, "w")
path =[ ]
path2 = [ ]
for rootDir, dirs, files in os.walk(args.p):
    for d in dirs:
        if 'coi' in dirs:
            path.append(os.path.join(rootDir, d))
            for i in path:
                output1.write("As of" + " " + str(today) + " " + "we have a coi folder for" + " " + str(i) + "\n")
        else:
            path2.append(os.path.join(rootDir, d))
            for m in path2:
                output2.write("As of" + " " + str(today) + " " + "we don't have a coi folder for" + " " + str(m) + "\n")
output1.close()
output2.close()
