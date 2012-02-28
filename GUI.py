import Tkinter

class GUI:

    def _init_(self):
        dim = 75
        master = Tkinter.Tk()
        Tkinter.Label(master, textvariable = "hey").pack()
        Tkinter.Button(master, text = "sup", command = "allahu akbar").pack()

        self.display = Tkinter.Canvas(master, bg = "green", width=600, height = 600)
        for i in range(1,8):
            val = 75 * i
            line = display.create_line(0, val, 600, val)
            line = display.create_line(val, 0, val, 600)
        oval = self.display.create_oval(3*dim,3*dim,4*dim,4*dim,fill="black")
        oval = self.display.create_oval(4*dim,4*dim,5*dim,5*dim,fill="black")
        oval = self.display.create_oval(3*dim,4*dim,4*dim,5*dim,fill="white")
        oval = self.display.create_oval(4*dim,3*dim,5*dim,4*dim,fill="white")

    def move(self, col, x, y):
        if col == 1:
            color = "white"
        elif col == -1:
            color = "black"
        oval = self.display.create_oval(x*dim,y*dim,(x+1)*dim,(y+1)*dim,fill=color)

    def flip(self, temp, x, y):
        if temp == 1:
            color = "white"
        elif temp == -1:
            color = "black"
        oval = self.display.create_oval(x*dim,y*dim,(x+1)*dim,(y+1)*dim,fill=color)

    Bob = GUI()
    move(-1, 2, 4)
    flip(-1, 3, 4)
    move(1, 2, 5)
    flip(1, 3, 4)

    display.pack()
    master.mainloop()


