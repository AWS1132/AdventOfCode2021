hor = 0
depth = 0
aim = 0
with open('AdventOfCode2021\day2puzz1.txt','r') as datafile:
    for line in datafile:
        print(line.split())
        if line.split()[0] == 'forward':
            hor += int(line.split()[1])
            depth += aim * int(line.split()[1])
        elif line.split()[0] == 'up':
            aim -= int(line.split()[1])
        elif line.split()[0] == 'down':
            aim += int(line.split()[1])
print(hor*depth)