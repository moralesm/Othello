#import GUI

class Game():

    def __init__(self, size):
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(0)

        #disp = GUI()
        board[3][3] = 1
        board[3][4] = -1
        board[4][4] = 1
        board[4][3] = -1
        self.board = board
        self.size = size
    
    def display(self):
        for i in range(self.size):
            print(self.board[i])
            print('')

    def isValid(self, x, y):
        if (x > (self.size-1) or x < 0 or y > (self.size-1) or y < 0):
            return False
        return True

    def checkDirection(self, x, y, i, j, color):
        captured = [((x+i),(y+j))]
        empty = []
        if(self.isValid((x + i),(y+j))):
            if (self.board[x+i][y+j] == (-1*color)):
                k = 2
                while (self.isValid((x+k*i),(y+k*j))):
                    if (self.board[x+k*i][y+k*j] == color):
                        return captured
                    if (self.board[x+k*i][y+k*j] == 0):
                        return empty
                    captured.append(((x+k*i),(y+k*j)))
                    k += 1
                return empty
            return empty
        return empty

    def findFlips(self, x, y, color):
        captured = []
        if (self.isValid(x,y)):
            if (self.board[x][y] == 0):
                for i in range(-1,2):
                    for j in range(-1, 2):
                        captured = captured + self.checkDirection(x,y,i,j,color)
        return captured
                            
    
    def playMove(self, x, y, color):
        flips = self.findFlips(x,y,color)
        self.board[x][y] = color;
        for elt in flips:
            self.board[elt[0]][elt[1]] *= -1

blah = Game(8)
blah.display()
blah.board[0][0] = 1
blah.board[1][1] = -1
blah.board[2][0] = 1
blah.board[2][1] = -1
print('--------------------')
blah.display()
blah.playMove(2,2, 1)
print('--------------------')
blah.display()


