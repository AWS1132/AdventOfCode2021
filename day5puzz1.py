with open('input2.txt') as file:
    data = [line.strip() for line in file]
field = [[0 for i in range(10)] for j in range(10)]

for line in data:
    x1,y1,x2,y2 = (line.replace(' ','').replace('->',',').split(',')) #this is shit lol
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    if x1==x2 or y1==y2:
        if x1>x2:
            x1,x2 = x2,x1
        if y1>y2:
            y1,y2 = y2,y1
        print(x1,y1," ",x2,y2)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                print(x,y)
                field[x][y] += 1
count = 0
for x in field:
    for y in x:
        if y>1:
            count += 1
print(count)
#this might be the ugliest thing ive written in forever
#will try to make better