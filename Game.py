
#Game board
board = []
#Move directions
dr = [1,1,1,0,0,-1,-1,-1]
dc = [1,0,-1,1,-1,1,0,-1]

class Game():

    #Initializing GameBoard
    def __init__(self):
        for i in range(8):
            board.append([])
            for j in range(8):
                board[i].append(0)
        
        board[3][3] = 1
        board[3][4] = -1
        board[4][4] = 1
        board[4][3] = -1
        self.board = board
    
    def printing(self):
        for i in range(8):
            print(board[i])
            print('')

    

    #Method checks for out of bounds
    def valid(self, r, c):
        if (r<0 or r>7 or c<0 or c>7):
            return False;
        return True;

    #Method will determine whether clicking on (r,c) is legal for 'color' player
    #Method will also fill in retrieve[][] with all pieces to color
    def is_legal(self, r, c, color):
        current = board[r][c]
        if current != 0:
            return False #already a piece here

        res = False;

        #list of pieces that have to be colored
        #temp is there so that only once the method is finished is 'retrieve'
        #altered, otherwise remains unchanged
        retrieve = [[],[],[],[],[],[],[],[]]
        temp = []
        
        #look in every direction
        for i in range(8):
            #check for out of bounds
            if self.valid(r + dr[i], c + dc[i])==False:
                continue
            #check that piece in dr[i] dc[i] direction is of opposite color
            if board[r + dr[i]][c + dc[i]] == -1*color:
                counter = 1
                activated = False
                while self.valid(r + counter*dr[i], c + counter*dc[i]):
                    if board[r + counter*dr[i]][c + counter*dc[i]] == -1*color:
                        temp.append([r + counter*dr[i], c + counter*dc[i]])
                        counter += 1
                    elif board[r + counter*dr[i]][c + counter*dc[i]] == color:
                        activated = True
                        retrieve[i] = temp
                        break
                    else: #reached blank spot before finding a piece of same color
                        break
                if activated:
                    res = True

        print retrieve
        return res


b = Game()
b.printing()
print b.is_legal(2,3,-1)


