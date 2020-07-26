from hangMan import *
from tkinter import *
game = Tk()


game.title("HangMan")

welcome = Label(game, text="Please Enter Your Name")
welcome.grid(column=5, row=1)

name = Entry(game, width=10)
name.grid(column=5, row=3)


def clicked():
    msg = Label(game, text="Let's Play HangMan" + name.get())
    msg.grid(column=5, row=4)


name_bt = Button(game, text='Submit', width=8, command=clicked)
name_bt.grid(column=5, row=6)


game.mainloop()
