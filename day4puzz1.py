with open('input.txt') as file:
    boards = []
    currentboard = []
    count = 0
    data = enumerate(file)
    for el in data:
        if el[0] == 0:
            input = el[1].split(',')
        else:
            if (el[1]) != '\n':
                currentboard.append(el[1].strip().split())
                count += 1
            if count == 5:
                boards.append(currentboard)
                currentboard = []
                count = 0

def checkbingo(binaryboard):
    columns = binaryboard
    rows = [[line[i] for line in binaryboard]for i in range(5)]
    for el in columns + rows:
        if el == ['1','1','1','1','1']:
            return True
    return False

def boardtobinaryboard(board,called):
    return [['1' if board[j][i] in called else '0' for i in range(5) ]for j in range(5)]

def scoreboard(board,binboard):
    score = 0
    unmarked = []
    for i in range(5):
        for j in range(5):
            if binboard[i][j] == '0':
                unmarked.append(board[i][j])
    for el in unmarked:
        score += int(el)
    return score * int(called[-1])
        
bingo = False
called = []
winningboard = []
while not bingo:
    called.append(input.pop(0))
    for board in boards:
        if checkbingo(boardtobinaryboard(board,called)):
            bingo = True
            winningboard = board

print(scoreboard(winningboard,boardtobinaryboard(winningboard,called)))
