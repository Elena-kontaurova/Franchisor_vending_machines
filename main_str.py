import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry('1124x700')
root.resizable(False, False)
root.title('Франчазер')

lala = tk.Label(root, background='white', width=160, height=3)
lala.place(x=0, y=0)
klk = tk.Label(root, background='#1e2329', width=40, height=50)
klk.place(x=0, y=50)
lkl = tk.Label(root, background='#060a0d', width=150, height=3)
lkl.place(x=285, y=50)
ksks = tk.Label(root, background='#060a0d', width=10, height=3)
ksks.place(x=206, y=50)
sls = tk.Label(root, background='white', border=2, relief='solid',
               width=20, height=3)
sls.place(x=1000, y=0)
# asd = tk.Label(text='Личный кабинет. Главная', font=('', 15))
# asd.place(x=300, y=110)
asd = tk.Label(root, text='Навигация', background='#1e2329', fg='#c4cacf',
               font=('', 13))
asd.place(x=10, y=62)
df = PhotoImage(file='frame12.png')
df = df.subsample(6)
ass = tk.Label(root, image=df, background='#1e2329')
ass.place(x=20, y=120)
dfd = PhotoImage(file='frame13.png')
dfd = dfd.subsample(6)
asff = tk.Label(root, image=dfd, background='#1e2329')
asff.place(x=20, y=180)


root.mainloop()
