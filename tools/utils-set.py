import os
import sys
import shutil

dir_path = sys.argv[1]
utils_path = os.path.join(os.path.dirname(__file__), '../src')

for f in os.listdir(utils_path):
    dir_f = os.path.join(dir_path, f)
    utils_f = os.path.join(utils_path, f)
    if not os.path.exists(dir_f):
        continue


    shutil.copy(dir_f, utils_f)
    print('cp ' + dir_f + ' ' + utils_f)

print('utils updated !')
    
    


