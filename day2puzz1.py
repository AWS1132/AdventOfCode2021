hor = 0
depth = 0
with open('day2puzz1.txt','r') as datafile:
    for line in datafile:
        print(line.split())
        if line.split()[0] == 'forward':
            hor += int(line.split()[1])
        elif line.split()[0] == 'up':
            depth -= int(line.split()[1])
        elif line.split()[0] == 'down':
            depth += int(line.split()[1])
print(hor*depth)