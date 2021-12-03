count = 0
prev = 0
with open('day1puzz1data.txt','r') as datafile:
    for line in datafile:
        if int(line) > prev:
            count+=1
        prev = int(line)
print(count-1)
