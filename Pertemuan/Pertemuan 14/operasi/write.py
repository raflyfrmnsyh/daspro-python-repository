# with open('folder/newFile.txt', 'r') as file :
#     print(file.read())

# with open('folder/newFile.txt', 'w') as file :
#     file.write("Tulisan ini yang akan ditulis kedalam berkas yang sudah ada")

# with open('folder/file.txt', 'a') as file :
#     file.write("Program untuk melakukan append")
print("\n---------------------------------------------******----------------------------------------------\n")
with open('folder/file.txt', 'r') as file :
    print(file.read())

# Write line
with open('folder/file.txt', 'w') as file:
    line = ["Ini\n", "adalah\n","tulisan\n","baru\n","dengan\n","metode\n", "writeline()"]
    file.writelines(line)

print("\n---------------------------------------------******----------------------------------------------\n")
with open('folder/file.txt', 'r') as file :
    print(file.read())
print("\n---------------------------------------------******----------------------------------------------\n")