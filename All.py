
from Tkinter import *
import Tkinter

#displays the actual game
class GUI():

    #creates the GUI object
    def __init__(self, game):
        self.dim = 75
        self.master = Tkinter.Tk()
        #Tkinter.Button(self.master, text = "sup", command = "allahu akbar").pack()

        def callback(event):
            print 'clicked at', event.x, event.y
            
            x = event.x/self.dim
            y = event.y/self.dim
            if len(game.findFlips(x,y,game.turn))!= 0:
                game.playMove(x,y,game.turn)
                game.turn *= -1
            game.display()
            game.display2(self)

            bcount = 0
            wcount = 0
            for i in range(game.size):
                for j in range(game.size):
                    if game.board[i][j] == 1:
                        wcount += 1
                    elif game.board[i][j] == -1:
                        bcount += 1
            if (game.canGo(game.turn) == False):
                #Tell the user that a player was skipped
                print ("Yo a playa wuz skipt")
                game.turn *= -1
            if (game.canGo(game.turn) == False):
                #Game over
                print ("Game over!")
                return
                            
            #Tkinter.Label(self.master, text = "Black player must pass\nWhite = " + \
             #         str(wcount) + "\tBlack = " + str(bcount)).pack()
            

        self.display = Tkinter.Canvas(self.master, bg = "green", width=600, height = 600)
        self.display.bind("<Button-1>", callback)
        self.draw()
        #oval = self.display.create_oval(3*dim,3*dim,4*dim,4*dim,fill="black")
        #oval = self.display.create_oval(4*dim,4*dim,5*dim,5*dim,fill="black")
        #oval = self.display.create_oval(3*dim,4*dim,4*dim,5*dim,fill="white")
        #oval = self.display.create_oval(4*dim,3*dim,5*dim,4*dim,fill="white")

    def draw(self):
        for i in range(1,8):
            val = self.dim * i
            line = self.display.create_line(0, val, 600, val)
            line = self.display.create_line(val, 0, val, 600)

    def showPiece(self, x, y, col):
        d = self.dim
        if col == 1:
            color = "white"
        elif col == -1:
            color = "black"
        oval = self.display.create_oval(x*d,y*d,(x+1)*d,(y+1)*d,fill=color)

                                       

class Game():

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
    
    def display(self):
        for i in range(self.size):
            print(self.board[i])
            print('')

    #places pieces on the board to resemble the matrix
    def display2(self, gui):
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] != 0):
                    gui.showPiece(i,j,self.board[i][j])

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
            
    def canGo(self, color):
        for i in range(8):
            for j in range(8):
                if (len(self.findFlips(i,j,color)) != 0):
                    return True
        return False

i=0
while(i<5):
    i += 1
    print ("Starting a game")
    g = Game(8)
    print ("-----------------------")
    testGUI = GUI(g)
    g.display2(testGUI)
    testGUI.display.pack()
    testGUI.master.mainloop()
