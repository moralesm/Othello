from Tkinter import *
import Tkinter

#displays the actual game
class GUI():

    #creates the GUI object
    def __init__(self, game):
        self.dim = 600/game.size
        self.game = game
        self.master = Tkinter.Tk()
        self.display = Tkinter.Canvas(self.master, bg = "green", width=600, height = 600)
        self.header = Tkinter.Canvas(self.master, bg = "white", width = 600, height = 30)
        self.words1 = self.header.create_text(300,10, text="It's Black's turn.", fill="blue")
        self.words2 = self.header.create_text(300,25, text="White: 2, Black: 2", fill = "red")
        self.header.pack()
        self.display.bind("<Button-1>", self.callback)
        self.draw()

    #draws the board
    def draw(self):
        for i in range(1,self.game.size):
            val = self.dim * i
            line = self.display.create_line(0, val, 600, val)
            line = self.display.create_line(val, 0, val, 600)

    #when the board is clicked, does all the important plays
    def callback(self,event):       
        x = event.x/self.dim
        y = event.y/self.dim
        #tests if a move is allowed (legal square, flips at least one enemy piece)
        if len(self.game.findFlips(x,y,self.game.turn))!= 0:
            self.game.playMove(x,y,self.game.turn)
            self.game.turn *= -1
        self.game.display2(self)
        bcount = 0
        wcount = 0
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.board[i][j] == 1:
                    wcount += 1
                elif self.game.board[i][j] == -1:
                    bcount += 1 #how many white and black pieces there are
        self.header.delete(self.words2)
        self.words2 = self.header.create_text(300,25, text = "White: " + str(wcount) + ", Black: " + str(bcount), fill = "red")
        if (self.game.canGo(self.game.turn) == False):
            self.game.turn *= -1
        if self.isGameOver(bcount, wcount, self.game):
            return
        self.turnDisplay(self.game)

    #changes a piece on the GUI
    def showPiece(self, x, y, col):
        d = self.dim
        if col == 1:
            color = "white"
        elif col == -1:
            color = "black"
        oval = self.display.create_oval(x*d,y*d,(x+1)*d,(y+1)*d,fill=color)

    #shows whose turn it is
    def turnDisplay(self, game):
            if (game.turn == 1):
                toplay = "White"
            else:
                toplay = "Black"
            self.header.delete(self.words1)
            self.words1 = self.header.create_text(300, 10, text = "It's " + toplay + "'s turn.", fill = "blue")

    #ends the game if it's over
    def isGameOver(self, bcount, wcount, game):
            if (game.canGo(game.turn) == False):
                #Game over
                if (bcount > wcount):
                    s = "Black wins!"
                elif (wcount > bcount):
                    s = "White wins!"
                else:
                    s = "Nobody wins!"
                self.header.delete(self.words1)
                self.words1 = self.header.create_text(300,10, text = "Game over! " + s, fill = "blue")
                return True
            return False
                            


#class for the mechanics of the game                                    
class Game():

    #makes a matrix to keep track of squares
    def __init__(self, size):
        board = []
        self.turn = -1
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(0)

        a = size/2
        board[a-1][a-1] = 1
        board[a-1][a] = -1
        board[a][a] = 1
        board[a][a-1] = -1
        self.board = board
        self.size = size

    #this would display the ASCII board
    """
    def display(self):
        for i in range(self.size):
            print(self.board[i])
            print('') """ 

    #places pieces on the board to resemble the matrix
    def display2(self, gui):
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] != 0):
                    gui.showPiece(i,j,self.board[i][j])

    #makes sure a square is on the board to avoid out of bounds
    def isValid(self, x, y):
        if (x > (self.size-1) or x < 0 or y > (self.size-1) or y < 0):
            return False
        return True

    #checks if a move works in a certain direction
    #needs enemy pieces followed by a friendly piece
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

    #sees which enemy pieces a move would flip
    def findFlips(self, x, y, color):
        captured = []
        if (self.isValid(x,y)):
            if (self.board[x][y] == 0):
                for i in range(-1,2):
                    for j in range(-1, 2):
                        captured = captured + self.checkDirection(x,y,i,j,color)
        return captured
                            
    #tries to play a certain move
    def playMove(self, x, y, color):
        flips = self.findFlips(x,y,color)
        self.board[x][y] = color;
        for elt in flips:
            self.board[elt[0]][elt[1]] *= -1

    #makes sure the player whose turn it is has a legal move           
    def canGo(self, color):
        for i in range(8):
            for j in range(8):
                if (len(self.findFlips(i,j,color)) != 0):
                    return True
        return False


g = Game(input("What dimension? Please type an even number"))
testGUI = GUI(g)
g.display2(testGUI)
testGUI.display.pack()
testGUI.master.mainloop()
