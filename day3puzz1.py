gamma = ''
epsilon = ''

def mostcommonspot(spot):
    with open('input.txt') as file:
        ones = 0
        zeros = 0
        for line in file:
            if line[spot]== '0':
                zeros += 1
            if line[spot] == '1':
                ones += 1
    if ones >= zeros:
        return '1'
    else:
        return '0'

def leastcommonspot(spot):
    with open('input.txt') as file:
        ones = 0
        zeros = 0
        for line in file:
            if line[spot]== '0':
                zeros += 1
            if line[spot] == '1':
                ones += 1
    if ones >= zeros:
        return '0'
    else:
        return '1'

for i in range(0,12):
    gamma += mostcommonspot(i)
    epsilon += leastcommonspot(i)


print(int(gamma,2) * int(epsilon,2))