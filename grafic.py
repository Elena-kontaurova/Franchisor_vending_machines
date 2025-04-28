import tkinter as tk


def graf():
    global c
    c = tk.PhotoImage(file='graf.png')
    c = c.subsample(3)
    return c


def svodk():
    global f
    f = tk.PhotoImage(file='svodka.png')
    f = f.subsample(3)
    return f


def graf_1():
    global d
    d = tk.PhotoImage(file='ipl_dua.png')
    d = d.subsample(2)
    return d


def graf_2():
    global d
    d = tk.PhotoImage(file='po_sum.png')
    d = d.subsample(2)
    return d
