import tkinter as tk


def graf():
    global c
    c = tk.PhotoImage(file='graf.png')
    c = c.subsample(3)
    return c
