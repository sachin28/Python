import os


def print_directory_contents(dirPath):

    for dirChild in os.listdir(dirPath):
        dirChildPath = os.path.join(dirPath,dirChild)
        if os.path.isdir(dirChildPath):
            print_directory_contents(dirChildPath)
        else:
            print(dirChildPath)

print_directory_contents("/Users/Sachin/Desktop/ExerciseFiles/Python/")