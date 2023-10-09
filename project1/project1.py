# Python Program designed to read hard drive space and display the total, used and free disk usage

#importing shutil Class
import shutil

#creating variables for the total, used, and free memory using shutil.disk_usage
totalMem, usedMem, freeMem = shutil.disk_usage("/")

#printing the total, used, and free memory calculated into GB
print("Total Memory: %d GB" % (totalMem // (1024**3)))
print("Used Memory: %d GB" % (usedMem // (1024**3)))
print("Free Memory: %d GB" % (freeMem // (1024**3)))

"""
Expected output should be
Total Memory: "Total" GB
Used Memory: "Used" GB
Free Memory: "Free" GB
"""
