from itertools import permutations
import time

start = time.perf_counter()

numbers = [list('123567'),list('36'),list('13457'),list('13467'),list('2346'),list('12467'),list('124567'),list('136'),list('1234567'),list('123467')]

with open('input.txt') as file:
    data = [[el[0].strip().split(),el[1].strip().split()] for el in [line.strip().split('|') for line in file]]

digitlist = []
for el in data:
    mapset = [set(number) for number in el[0]] #a list of sets where each set is a signal sent
    for wiremap in permutations(list('abcdefg')):
        reslist = []
        for number in numbers:
            currentnum = ''
            for segments in number:
                currentnum += wiremap[int(segments)-1]
            reslist.append(currentnum)
        resset = [set(number) for number in reslist]
        count = ''
        for number in resset:
            flag = True
            for number2 in mapset:
                if flag:
                    if (number==number2):
                        count += str(resset.index(number))
                        flag = False

        if len(count) == 10:
            fourdigit = ''
            digitdisplay = [set(number) for number in el[1]]
            for digit in digitdisplay:
                fourdigit+=str((resset.index(digit)))
            digitlist.append(int(fourdigit))
            break
    print(digitlist)

print(sum(digitlist))

stop = time.perf_counter()

print(stop-start)