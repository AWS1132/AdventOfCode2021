with open('input.txt') as file:
    data = [line.strip() for line in file]
field = [[0 for i in range(1010)] for j in range(1000)]

def longer(list1,list2):
    if len(list1) >=len(list2):
        return list1
    else:
        return list2

for line in data:
    x1,y1,x2,y2 = (line.replace(' ','').replace('->',',').split(',')) #this is shit lol
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    if (x1==x2) or (y1==y2) or ((x1<x2) == (y1<y2)):
        points = [[x,y] for y in longer(range(y1,y2+1),range(y2,y1+1)) for x in longer(range(x1,x2+1),range(x2,x1+1)) if (y1-y == x1-x) or (x1==x2 or y1==y2)]
    else:
        if x1<x2 and y1>y2:
            points = [[x,y] for y in range(y1,y2-1,-1) for x in range(x1,x2+1) if x+y == x1+y1]
        elif x1>x2 and y1<y2:
            points = [[x,y] for y in range(y1,y2+1) for x in range(x1,x2-1,-1) if x+y == x1+y1]
    for el in points:
        field[el[0]][el[1]] += 1
            
count = 0
for x in field:
    for y in x:
        if y>1:
            count += 1
print(count)
#this might be the ugliest thing ive written in forever
#will try to make better