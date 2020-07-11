import os
import sys

foldername = str(sys.argv[1])
path = r"E:\z-React Apps"
dir = path + '\\'+ foldername

os.chdir(path)
if os.path.isdir(foldername):
    print("Folder with same name already exists")
else:
    os.system(f'npx create-react-app {foldername} --use-npm')
    os.chdir(dir)
    os.system('code .')
    print(f' Project {foldername} created successfully')
