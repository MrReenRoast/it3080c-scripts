import os

print('What is the path/file you want to look up?')
pathName = input()
pathSize = os.stat(pathName)
if pathName.is_file():
    print('Here is the size of your file: ' + str(pathSize.st_size) + ' bytes')
elif pathName.is_dir():
    for root, dirs, files in os.walk(pathName):
        for f in files:

        for d in dirs:
