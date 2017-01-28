import os

# path = "/Users/Sachin/Desktop"
ask_user = True

while (ask_user):
    try:
        path = raw_input("Enter the path to list the directories: ")
        dir = os.listdir(path)
        ask_user = False
    except:
        print "Directory does not exist"

myfile = open('directories.txt', 'w')

for file in dir:
    #   print file
    myfile.writelines(file)
    myfile.write("\n")

myfile.close()
