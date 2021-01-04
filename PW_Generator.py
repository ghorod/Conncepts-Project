# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import random, string
import pyperclip


root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of our password:")



def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()


lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

#
val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

# passprint


def callback():
    lsum.config(text=passgen())

def copy():
    pyperclip.copy(newpass)


# clickable button
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)
copyButton = Button(root, text="Copy Password", bd=5, height=2, command=copy, pady=3)
copyButton.pack()

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
    global newpass
    if choice.get() == 1:
        newpass = "".join(random.sample(poor, val.get()))
        return newpass
    elif choice.get() == 2:
        newpass = "".join(random.sample(average, val.get()))
        return newpass
    elif choice.get() == 3:
        newpass = "".join(random.sample(advance, val.get()))
        return newpass


root.mainloop()