import os

print('What is the path/file you want to look up?')
pathName = input()
try:
    pathSize = os.stat(pathName)
except:
    print("You entered a blank directory")
file_list = []
fileSize = 0
for root, dirs, files in os.walk(pathName):
    for f in files:
        file_list.append([os.path.join(root, f), os.stat(os.path.join(root, f)).st_size])
        fileSize += int(os.stat(os.path.join(root, f)).st_size)
file_list.sort(key=lambda x: x[1], reverse=True)
print("Path Size(bytes) Percent")
print("-----------------------------------------------------------------------")
for f in file_list:
    print(f[0], f[1], str(round(f[1]/fileSize*100, 2)) + "%")
print("Here is the total size of the directory: " + str(fileSize) + " MB")
