import tkinter as tk


def graf():
    # бим
    global c
    c = tk.PhotoImage(file='kartinka/graf.png')
    c = c.subsample(3)
    return c


def svodk():
    # дим
    global f
    f = tk.PhotoImage(file='kartinka/svodka.png')
    f = f.subsample(3)
    return f


def graf_1():
    # мне не двадцать 
    global d
    d = tk.PhotoImage(file='kartinka/ipl_dua.png')
    d = d.subsample(2)
    return d


def graf_2():
    global d
    d = tk.PhotoImage(file='kartinka/po_sum.png')
    d = d.subsample(2)
    return d
