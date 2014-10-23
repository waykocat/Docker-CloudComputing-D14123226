from os import listdir
from os.path import isfile, join
import sys

directories = str(sys.argv[1])
onlyfiles = [ f for f in listdir("./"+directories+"/") if isfile(join("./"+directories+"/",f))]
print onlyfiles
for i in onlyfiles:
    print i
