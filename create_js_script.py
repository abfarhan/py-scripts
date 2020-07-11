import os
import sys

foldername = str(sys.argv[1])
path = r"E:\z-Js Apps"
dir = path + '\\'+ foldername

os.chdir(path)
if os.path.isdir(foldername):
    print("Folder with same name already exists")
else:
    os.mkdir(dir)
    os.chdir(dir)
    open('index.html', 'w')
    open('script.js', 'w')
    open('style.css', 'w')
    os.system('code .')
    print(f' Project {foldername} created successfully')
