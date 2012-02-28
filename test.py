from Tkinter import *

root = Tk()
frame = Frame(root, width=300, height=300)

def callback(event):
    print 'new'
    print "clicked at", event.x, event.y

frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
