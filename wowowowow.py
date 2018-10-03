from tkinter import *
from random import *
import time

def do_event(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    global k
    app.hello_b.place(relx=random(),rely=random())
    k += 1
    if k == 2:
        while 1:
            app.hello_b.place(relx=random(),rely=random())
    print(k)

class App:
    def __init__(self,master):
        global k
        frame = Frame(master)
        master.geometry("160x160")
        master.title("My first program!")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        print(k)
        frame.pack()

        self.hello_b = Button(master,text="Quit",command=sys.exit)
        self.hello_b.bind("<Enter>",jump)
        self.hello_b.pack()
        print(k)


k = 0

root = Tk()

app = App(root)

root.mainloop()
