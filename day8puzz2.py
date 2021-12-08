from itertools import permutations
numbers = ['123567','36','13457','13467','2346','12467','124567','136','1234567','123467']
with open('input.txt') as file: data = [[el[0].strip().split(),el[1].strip().split()] for el in [line.strip().split('|') for line in file]]
digitlist = []
for el in data:
    for wiremap in permutations(list('abcdefg')):
        resset = ([set(number) for number in [[wiremap[int(segments)-1] for segments in number] for number in numbers]])
        if len([" " for number2 in [set(number) for number in el[0]] for number in resset if number==number2])==10:
            digitlist.append(int(str([str((resset.index(digit)))for digit in [set(number) for number in el[1]]]).replace("', '",'')[2:6]))
            break
print(sum(digitlist))