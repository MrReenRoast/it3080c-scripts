import os
import matplotlib.pyplot as plt

quitApp = "y"
#ask user for the path
print('What is the path you want to look up? (Type n to close)')
pathName = input()
while quitApp != "n":
    if pathName == "n":
        raise SystemExit
    #failsafe for blank directory
    while pathName != "n":
        try:
            pathSize = os.stat(pathName)
            break
        except:
            print("You entered a blank or nonexistent directory. Please enter a correct directory")
            pathName = input()
    #adding variables
    file_list = []
    fileSize = 0
    #this code looks up the directory and subdirectories, then gets the file name and size of all the files in the directory
    for root, dirs, files in os.walk(pathName):
        for f in files:
            file_list.append([os.path.join(root, f), os.stat(os.path.join(root, f)).st_size])
            fileSize += int(os.stat(os.path.join(root, f)).st_size)
    #this sorts the files by largest size first
    file_list.sort(key=lambda x: x[1], reverse=True)
    #outputs the files in a readable format and calculates the percentage of space it takes up
    print("Path Size(bytes) Percent")
    print("-----------------------------------------------------------------------")
    nameArray = []
    sizeArray = []
    for f in file_list:
        print(f[0], f[1], str(round(f[1]/fileSize*100, 2)) + "%")
        nameArray.append(f[0])
        sizeArray.append(f[1])
    plt.pie(sizeArray, labels = nameArray)
    plt.show()
    print("Here is the total size of the directory: " + str(fileSize/1024**3) + " GB")
    #Allows user to put in more directories or quit
    print("Would you like to search another directory? (y/n)")
    quitApp = input()
    if quitApp == "n":
        break
    elif quitApp == "y":
        print('What is the path you want to look up? (Type n to close)')
        pathName = input()
    else:
        print("That is not a valid input. Please only use y or n")
        quitApp = input()