with open('file1.txt', 'r') as fileReader:
    count=0
    for line in fileReader:
        count+=1

print(f"Total number of lines: {count}")