import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.geometry('500x500')
mdvkar = PhotoImage(file='image_inform/mdvkar.png')
mdvkar = mdvkar.subsample(30)
nast = PhotoImage(file='image_inform/nast.png')
nast = nast.subsample(14)
oblak = PhotoImage(file='image_inform/oblak.png')
oblak = oblak.subsample(22)

for i in range(4):
    one = tk.Label(root, background='green', width=28, height=3)
    one.pack(padx=10, pady=10)
    mdv = tk.Label(one, image=mdvkar)
    mdv.place(x=0, y=0)
    na = tk.Label(one, image=nast)
    na.place(x=100, y=0)
    obl = tk.Label(one, image=oblak)
    obl.place(x=145, y=0)

root.mainloop()
