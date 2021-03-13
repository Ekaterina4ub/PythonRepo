# print line from testfile.txt # where "TestString" exists

with open('testfile.txt') as file:
    count = 0
    for i in file:
        if "TestString" in i:
            count += 1
            print(count)
        else:
            count += 1
