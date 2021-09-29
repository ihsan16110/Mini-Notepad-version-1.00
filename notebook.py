import tkinter
from tkinter import Entry, font
from tkinter.constants import BOTH, END, INSERT, LEFT, TRUE, WORD
from tkinter.filedialog import *
import tkinter as tk
from typing import Text

def saveFile():
    new_file= asksaveasfile(mode = 'w' , filetype=[('text files', '.txt')])
    if new_file is None:
        return

    text =str(tkinter.entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode= 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content =file.read()

    Entry.insert(INSERT, content)



def ClearFile():
    Entry.delete(1.0, END)


canvas= tk.Tk()
canvas.geometry("400x600")
canvas.title("Notebook")
canvas.config(bg="white")
top= tkinter.Frame(canvas)
top.pack(padx=10,pady=5,anchor='nw')

b1 = tkinter.Button(canvas, text="Open" , bg="white" , command=openFile)
b1.pack(in_ = top, side=LEFT)

b2 = tkinter.Button(canvas, text="Save" , bg="white", command=saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = tkinter.Button(canvas, text="Clear" , bg="white", command=ClearFile)
b3.pack(in_ = top, side=LEFT)

b4 = tkinter.Button(canvas, text="Exit" , bg="white", command=exit)
b4.pack(in_ = top, side=LEFT)

tkinter.entry = Text (canvas,wrap= WORD, bg="#F9DDA4", font = ("poppins",15))
tkinter.entry.pack (padx= 10, pady=5 ,expand = TRUE, fill = BOTH)

canvas.mainloop()