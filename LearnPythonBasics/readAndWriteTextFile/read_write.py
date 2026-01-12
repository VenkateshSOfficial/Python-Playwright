source_file=open("test.txt")
# read all contents of the file
# print(source_file.read())

# read single line using the readLine() function
# print(source_file.readline())

#line=source_file.readline()
#while line!="":
 #   print(line)
 #   line=source_file.readline()

for line in source_file.readlines():
    print(line)

source_file.close()