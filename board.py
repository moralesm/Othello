size = 8
board = []

for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(0)

board[3][3] = 1
board[3][4] = -1
board[4][4] = 1
board[4][3] = -1

class Board:
    
    def display():
        for i in range(size):
            print(board[i])
            print('\n')

    display()

    def isValid(x):
        if (x > 7 or x < 0):
            return False
        return True
            
    def isLegal(x, y):
        isLegal = False
        for i in range(-1,2):
            for j in range(-1, 2):
                if(isValid(x + i) and isValid(y + j)):
                    print 7
                
