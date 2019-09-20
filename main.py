import sys
import os

arr = sys.argv[1::]

for a in arr:
    
    cmd = "python new_task.py {}".format(a)
    print(cmd)
    os.system(cmd)


