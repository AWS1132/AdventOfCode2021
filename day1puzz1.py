count = 0
prev = 100000000
with open('day1puzz1data.txt','r') as datafile:
    for line in datafile:
        if int(line) > prev:
            print(f'{line.strip()} increased')
            count+=1
        else:
            print(f'{line.strip()} decreased')
        prev = int(line)
print(count-1)
