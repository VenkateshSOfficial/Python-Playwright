# with open('text.txt','r') as file:
#     content = file.read()
#     print(content)
#
# with open('text.txt','f') as f:
#     data=f.readline()
#     print(data)
#
# with open('text.txt','r') as f:
#     val=f.readlines()
#     print(val)

# read the file, store in list, reverse and write back to another text

with open('test.txt','r') as fileReader:
    lines = fileReader.readlines()
    print('Tye of line is : ' , type(lines))
    reversed_lines=reversed(lines)
    with open('test.txt','w') as fileWriter:
        for line in reversed_lines:
            fileWriter.write(line+'\n')
