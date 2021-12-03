with open('input.txt') as file:
    olist = [line.strip() for line in file]
with open('input.txt') as file:
    clist = [line.strip() for line in file]

def mostcommonspot(spot,list):
    ones = 0
    zeros = 0
    for line in list:
        if line[spot]== '0':
            zeros += 1
        if line[spot] == '1':
            ones += 1
    if ones >= zeros:
        return '1'
    else:
        return '0'

def leastcommonspot(spot,list):
    ones = 0
    zeros = 0
    for line in list:
        if line[spot]== '0':
            zeros += 1
        if line[spot] == '1':
            ones += 1
    if ones >= zeros:
        return '0'
    else:
        return '1'

ox = ''
car = ''

for i in range(0,12):
    goodlist=[]
    mostcommon = mostcommonspot(i,olist)
    for line in olist:
        if line[i] == mostcommon:
            goodlist.append(line)
    if len(goodlist) == 1:
        ox = goodlist[0] 
    olist = goodlist

for i in range(0,12):
    goodlist=[]
    leastcommon = leastcommonspot(i,clist)
    for line in clist:
        if line[i] == leastcommon:
            goodlist.append(line)
    if len(goodlist) == 1:
        car = goodlist[0] 
    clist = goodlist 

print(int(ox,2) * int(car,2))