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

def one_ychet_1():
    global a
    a = tk.PhotoImage(file='diagramm_ychet/iag_raskod_str1.png')
    a = a.subsample(3)
    return a

def two_ychet_1():
    global aa
    aa = tk.PhotoImage(file='diagramm_ychet/spros_str1.png')
    aa = aa.subsample(3)
    return aa

def three_ychet_1():
    global aaa
    aaa = tk.PhotoImage(file='diagramm_ychet/proc1_str1.png')
    aaa = aaa.subsample(3)
    return aaa

def fo_ychet_1():
    global aaaa
    aaaa = tk.PhotoImage(file='diagramm_ychet/proc2_str1.png')
    aaaa = aaaa.subsample(3)
    return aaaa
