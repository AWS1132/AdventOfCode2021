count = 0
prev = 1000000
with open('day1puzz1data.txt','r') as datafile:
    content = datafile.readlines()
    for i in range(len(content)-2):
        current = int(content[i])+ int(content[i+1]) + int(content[i+2])
        if current > prev:
            print(f'{current}, increased')
            count += 1
        else:
            print(f'{current}, decreased')
        prev = current
print(count)