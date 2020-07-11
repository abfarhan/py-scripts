import os
import sys

foldername = str(sys.argv[1])
path = r"E:\z-Angular Apps"
dir = path + '\\'+ foldername
skipInstall = ""

if len(sys.argv) == 3:
    if str(sys.argv[2]) == "--skip-install":
        skipInstall = str(sys.argv[2])

os.chdir(path)
if os.path.isdir(foldername):
    print("Folder with same name already exists")
else:
    os.system(f'ng new {foldername} {skipInstall}') if skipInstall !="" else os.system(f'ng new {foldername}')
    # os.system(f'ng new {foldername} --use-npm')
    os.chdir(dir)
    os.system('code .')
    print(f' Project {foldername} created successfully')
