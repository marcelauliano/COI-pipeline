import sys
import os
import shutil

path = ['/Users/mu2/Sanger/COI/test19020202', '/Users/mu2/Sanger/COI/test19020202/outro']
files= [ ]
for l in path:
        list = os.listdir(l)
        files = files + list
        for obj in files:
                if obj.endswith(".py-e"):
                        newPath = shutil.copy(obj, '/Users/mu2/Sanger/COI/test19020202/testiculo')
                        print(newPath)
