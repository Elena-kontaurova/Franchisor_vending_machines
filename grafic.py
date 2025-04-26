import tkinter as tk


def graf():
    # бим
    global c
    c = tk.PhotoImage(file='graf.png')
    c = c.subsample(3)
    return c


def svodk():
    global f
    f = tk.PhotoImage(file='svodka.png')
    f = f.subsample(3)
    return f
