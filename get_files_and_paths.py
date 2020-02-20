import sys
import shutil

#My idea here is, giving a list of paths to directories, go to each one of them, if the files on them end with "gz", I would like to copy this file to a specific directory, and I would like to print (or save to a file) the path where it came from + the name of the file. I just thought that for this second problem, maybe I should use a dictionary?

path = ['/Users/mu2/Sanger/COI/test19020202', '/Users/mu2/Sanger/COI/test19020202/outro']
files= [ ]
for l in path:
        list = os.listdir(l)
        files = files + list
        for obj in files:
                if obj.endswith(".gz"):
                        newPath = shutil.copy(obj, '/Users/mu2/Sanger/COI/test19020202/testiculo')
                        print(newPath)
#with this code for now, I'm going round the loop looking into the paths listed on the list, and trying to copy them to the path on newPath. Funny thing is that python lists the files on the paths and inputs it to my list "files", but when it trys to copy the obj in the second for loop, it does not find the file in the second path, because I guess shut.util only seems things in the current directory.
#My question is: do you think this is a good way to go, or would you do things drastically diferrently? If yes, could you give my a way forward?

#for now, one of my challenge is: find a way to list, find the file, and in this exact moment copy to the newpath, without inputing to the list "files"?
