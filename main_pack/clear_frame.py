def clear_fun(frame):
    for widget in frame.winfo_children():
        print(widget)
       # widget.destroy()


# !/usr/bin/python
# -*- coding: UTF-8 -*-
# python2  使用 Tkinter
from tkinter import *


# python3 使用 tkinter
# from tkinter import *
def say_hi():
    print("hello ~ !")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
root.title("tkinter frame")

label = Label(frame1, text="Label", justify=LEFT)
label.pack(side=LEFT)

hi_there = Button(frame2, text="say hi~", command=say_hi)
hi_there.pack()

frame1.pack(padx=1, pady=1)
frame2.pack(padx=10, pady=10)
clear_fun(frame1)
clear_fun(frame2)
root.mainloop()