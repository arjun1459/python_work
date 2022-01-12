# import OS module
import os

# Get the list of all files and directories
path = "F://data//yify//"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
for file in dir_list:
    print(file)

# print(dir_list)
