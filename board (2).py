class Board():

    def __init__(self, size):
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(0)

        board[3][3] = 1
        board[3][4] = -1
        board[4][4] = 1
        board[4][3] = -1
        self.board = board
        self.size = size
    
    def display(self):
        for i in range(self.size):
            print(self.board[i])
            print('\n')

    def isValid(self, x):
        if (x > (self.size-1) or x < 0):
            return False
        return True

    def checkDirection(self, x, y, i, j, color):
        if(self.isValid(x + i) and self.isValid(y + j)):
            if (self.board[x+i][y+j] == (-1*color)):
                k = 2
                while (self.isValid(x+k*i) and self.isValid(y+k*j)):
                    if (self.board[x+k*i][y+k*j] == color):
                        return True
                    k += 1
                return False
            return False
        return False

    def isLegal(self, x, y, color):
        for i in range(-1,2):
            for j in range(-1, 2):
                if (self.checkDirection(x, y, i, j, color) == True):
                    return True
        return False
                            

blah = Board(8)
blah.display()
print blah.isLegal(2,4,-1)
