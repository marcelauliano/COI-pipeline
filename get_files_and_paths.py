import sys
import shutil
import os

path = ['/Users/mu2/Sanger/COI/test19020202', '/Users/mu2/Sanger/COI/test19020202/outro']
for l in path:
        list = os.listdir(l)
        for obj in list:
                if obj.endswith(".gz"):
                        newPath = shutil.copy(l + "/" + obj, '/Users/mu2/Sanger/COI/test19020202/testiculo')
                        print(newPath)
