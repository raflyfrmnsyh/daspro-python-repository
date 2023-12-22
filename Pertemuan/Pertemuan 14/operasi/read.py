# read method
file = open('folder/file.txt', 'r')
content = file.read()
print(content)
print("======================================")

# readline method
with open('folder/file.txt', 'r') as withFile:
    line = withFile.readline()
    while line :
        print(line)
        line = withFile.readline()
    print("======================================")   

with open('folder/file.txt', 'r') as fileText :
    for line in fileText:
        print(line)