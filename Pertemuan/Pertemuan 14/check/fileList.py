import os

path = "folder/fileList.txt"

if os.path.isfile(path):
    with open(path,"r") as file :
        lines = file.readlines()

    listData = []
    for line in lines:
        newLine = line.strip().split()
        listData.append(newLine)
    
    for i in listData:
        print(i)