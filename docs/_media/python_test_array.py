import sys
import os
import time
time.sleep(10)

file_name = "file_{}.txt".format(sys.argv[1])
with open(file_name,'w') as fileOut:
    print("this is my {} job".format(sys.argv[1]), file=fileOut)
