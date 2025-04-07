import tkinter as tk
from tkinter import PhotoImage
from connect import Svodka, News

root = tk.Tk()
root.geometry('1124x700')
root.resizable(False, False)
root.title('Франчазер')


def get_svodka():
    svodka = Svodka.select()
    return svodka


def get_news():
    news = News.select()
    return news


def open_main_str(_):
    ''' Личный кабинет главная'''
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Главная',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=1050, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)
    kk = tk.Label(hh, text='Личный кабинет. Главная',
                  background='#c4cacf', font=('', 15))
    kk.place(x=20, y=20)
    kv1 = tk.Label(hh, width=32, height=12, background='white')
    kv1.place(x=20, y=60)
    pl_k1 = tk.Label(hh, width=32, height=3, background='#d1d8de')
    pl_k1.place(x=20, y=60)
    t1 = tk.Label(pl_k1, text='Эффективность сети', background='#d1d8de',
                  font=('', 11))
    t1.place(x=4, y=9)
    tex_avt = tk.Label(kv1, text='тут эффективность сети',
                       background='white')
    tex_avt.place(x=46, y=100)

    kv2 = tk.Label(hh, width=32, height=12, background='white')
    kv2.place(x=300, y=60)
    pl_k2 = tk.Label(hh, width=32, height=3, background='#d1d8de')
    pl_k2.place(x=300, y=60)
    t2 = tk.Label(pl_k2, text='Состояние сети', background='#d1d8de',
                  font=('', 11))
    t2.place(x=4, y=9)
    tex_avt = tk.Label(kv2, text='тут состояние сети',
                       background='white')
    tex_avt.place(x=46, y=100)

    kv3 = tk.Label(hh, width=32, height=12, background='white')
    kv3.place(x=580, y=60)
    pl_k3 = tk.Label(hh, width=32, height=3, background='#d1d8de')
    pl_k3.place(x=580, y=60)
    t3 = tk.Label(pl_k3, text='Сводка', background='#d1d8de',
                  font=('', 11))
    t3.place(x=4, y=9)
    svo = get_svodka()

    y_position = 52
    for i in svo:
        a = tk.Label(kv3, text=f'{i.name}', background='white',
                     font=('', 6))
        a.place(x=10, y=y_position)
        b = tk.Label(kv3, text=f'{i.price}', background='white',
                     font=('', 6))
        b.place(x=170, y=y_position)
        y_position += 15

    kv4 = tk.Label(hh, width=72, height=17, background='white')
    kv4.place(x=20, y=280)
    pl_k4 = tk.Label(hh, width=72, height=6, background='#d1d8de')
    pl_k4.place(x=20, y=280)
    t4 = tk.Label(pl_k4, text='Динамика продаж за последние 10 дней',
                  background='#d1d8de',
                  font=('', 11))
    t4.place(x=4, y=9)
    tete = tk.Label(pl_k4,
                    text='Данные по продажам с 1.03.2025 по 10.03.2025',
                    background='#d1d8de',
                    font=('', 7),
                    fg='#686b6e')

    def cd_blu(_):
        knop.config(background='#1870b8')
        knop1.config(background='white')
        hhk.config(background='#1870b8', fg='white')
        hhn.config(background='white', fg='black')

    def cd_hh(_):
        knop1.config(background='#1870b8')
        knop.config(background='white')
        hhn.config(background='#1870b8', fg='white')
        hhk.config(background='white', fg='black')

    tete.place(x=4, y=37)
    knop = tk.Label(pl_k4, width=18, height=1, background='#1870b8')
    knop.place(x=4, y=60)
    hhk = tk.Label(knop, text='По суммe', background='#1870b8', fg='white')
    hhk.place(x=32, y=0)
    knop.bind('<Button-1>', cd_blu)

    knop1 = tk.Label(pl_k4, width=18, height=1, background='white')
    knop1.place(x=140, y=60)
    hhn = tk.Label(knop1, text='По количеству', background='white', fg='black')
    hhn.place(x=24, y=0)
    knop1.bind('<Button-1>', cd_hh)

    kv5 = tk.Label(hh, width=32, height=17, background='white')
    kv5.place(x=580, y=280)
    pl_k5 = tk.Label(hh, width=32, height=3, background='#d1d8de')
    pl_k5.place(x=580, y=280)
    t5 = tk.Label(pl_k5, text='Новости', background='#d1d8de',
                  font=('', 11))
    t5.place(x=4, y=9)

    news = get_news()
    y_posi = 53
    for i in news:
        c = tk.Label(kv5, text=f'{i.date}', background='white',
                     font=('', 6))
        c.place(x=10, y=y_posi)
        d = tk.Label(kv5, text=f'{i.text}', background='white',
                     font=('', 6))
        d.place(x=60, y=y_posi)
        y_posi += 30


def open_monik_str(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Монитор ТА',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=1025, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_det_otc_str_1(_):
    ff = tk.Label(root, background='#060a0d', width=70, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Детальные отчеты/ Отчет 1',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=905, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_det_otc_str_2(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Детальные отчеты/ Отчет 2',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=905, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_det_otc_str_3(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=900, y=50)
    gg = tk.Label(root, text='Детальные отчеты / Отчет 3',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=905, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_ychet_1(_):
    ff = tk.Label(root, background='#060a0d', width=70, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Учет ТМЦ / Учет 1',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=975, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_ychet_2(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Учет ТМЦ / Учет 2',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=975, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_ychet_3(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Учет ТМЦ/ Учет 3',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=975, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_torg_avt(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Торговые автоматы',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=800, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_komp(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Компании',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=870, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_polsov(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Пользователи',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=850, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_modem(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Модемы',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=890, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_dop(_):
    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Дополнительные',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=830, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)


def open_pod_menu_detot(_):
    global atsosite
    lkj.place(x=10, y=380)
    sdf.place(x=10, y=440)
    hhhhg.place(x=65, y=390)
    hhhhh.place(x=65, y=450)
    ff2.place(x=250, y=390)
    ff3.place(x=250, y=450)
    ff1.config(image=soss)
    atsosite = tk.Label(root, background='#0b1217',
                        width=40, height=5)
    atsosite.place(x=0, y=300)
    tt = tk.Label(atsosite, text='Отчет 1', background='#0b1217',
                  fg='white', font=('', 10))
    tt.place(x=30, y=10)
    tt.bind('<Button-1>', open_det_otc_str_1)
    tg = tk.Label(atsosite, text='Отчет 2', background='#0b1217',
                  fg='white', font=('', 10))
    tg.place(x=30, y=30)
    tg.bind('<Button-1>', open_det_otc_str_2)
    tf = tk.Label(atsosite, text='Отчет 3', background='#0b1217',
                  fg='white', font=('', 10))
    tf.place(x=30, y=50)
    tf.bind('<Button-1>', open_det_otc_str_3)


def open_pod_menu_ychet(_):
    global ststs
    sdf.place(x=10, y=440)
    hhhhh.place(x=65, y=450)
    ff3.place(x=250, y=450)
    ff2.config(image=soss)
    ststs = tk.Label(root, background='#0b1217',
                     width=40, height=5)
    ststs.place(x=0, y=350)
    tt = tk.Label(ststs, text='Учет 1', background='#0b1217',
                  fg='white', font=('', 10))
    tt.place(x=30, y=10)
    tt.bind('<Button-1>', open_ychet_1)
    tg = tk.Label(ststs, text='Учет 2', background='#0b1217',
                  fg='white', font=('', 10))
    tg.place(x=30, y=30)
    tg.bind('<Button-1>', open_ychet_2)
    tf = tk.Label(ststs, text='Учет 3', background='#0b1217',
                  fg='white', font=('', 10))
    tf.place(x=30, y=50)
    tf.bind('<Button-1>', open_ychet_3)


def open_pod_menu_admin(_):
    global ssss
    ff3.config(image=soss)
    ssss = tk.Label(root, background='#0b1217',
                    width=40, height=10)
    ssss.place(x=0, y=410)
    tt = tk.Label(ssss, text='Торговые автоматы', background='#0b1217',
                  fg='white', font=('', 10))
    tt.place(x=30, y=10)
    tt.bind('<Button-1>', open_torg_avt)
    tg = tk.Label(ssss, text='Компании', background='#0b1217',
                  fg='white', font=('', 10))
    tg.place(x=30, y=30)
    tg.bind('<Button-1>', open_komp)
    tf = tk.Label(ssss, text='Пользователи', background='#0b1217',
                  fg='white', font=('', 10))
    tf.place(x=30, y=50)
    tf.bind('<Button-1>', open_polsov)
    hh = tk.Label(ssss, text='Модемы', background='#0b1217',
                  fg='white', font=('', 10))
    hh.place(x=30, y=70)
    hh.bind('<Button-1>', open_modem)
    hs = tk.Label(ssss, text='Дополнительные', background='#0b1217',
                  fg='white', font=('', 10))
    hs.place(x=30, y=90)
    hs.bind('<Button-1>', open_dop)


def close_pod_menu_detot(_):
    global atsosite
    lkj.place(x=10, y=300)
    sdf.place(x=10, y=360)
    hhhhg.place(x=65, y=310)
    hhhhh.place(x=65, y=370)
    ff2.place(x=250, y=310)
    ff3.place(x=250, y=370)
    atsosite.destroy()
    ff1.config(image=galka)


def close_pod_menu_ychet(_):
    global ststs
    sdf.place(x=10, y=360)
    hhhhh.place(x=65, y=370)
    ff3.place(x=250, y=370)
    ststs.destroy()
    ff2.config(image=galka)


def close_pod_menu_adnim(_):
    global ssss
    ssss.destroy()
    ff3.config(image=galka)


lala = tk.Label(root, background='white', width=160, height=3)
lala.place(x=0, y=0)

klk = tk.Label(root, background='#1e2329', width=40, height=50)
klk.place(x=0, y=50)


lkl = tk.Label(root, background='#060a0d', width=150, height=3)
lkl.place(x=285, y=50)


ddd = tk.Label(root, text='ООО Торговые Автоматы',
               background='#060a0d', fg='white',
               font=('', 15))
ddd.place(x=290, y=60)

sls = tk.Label(root, background='white', border=2, relief='solid',
               width=20, height=3)
sls.place(x=980, y=0)
ttt = tk.Label(sls, text='Контаурова Е.С', background='white',
               fg='black')
ttt.place(x=40, y=5)
tt = tk.Label(sls, text='Администратор', background='white',
              fg='#7f8182')
tt.place(x=40, y=20)
one = tk.Label(sls, width=2, background='#c7c7c7')
one.place(x=7, y=13)
one = tk.Label(sls, width=2, background='#2809ed')
one.place(x=7, y=18)
one = tk.Label(sls, width=2, background='#ed1826')
one.place(x=7, y=25)
one = tk.Label(sls, width=2, background='#fff')
one.place(x=7, y=31)
one = tk.Label(sls, width=2, background='#060a0d')
one.place(x=7, y=47)

ksks = tk.Label(root, background='#060a0d', width=10, height=3)
ksks.place(x=206, y=50)
menu = PhotoImage(file='menu.png')
menu = menu.subsample(5)
dd = tk.Label(root, image=menu, background='#060a0d')
dd.place(x=215, y=55)
# asd = tk.Label(text='Личный кабинет. Главная', font=('', 15))
# asd.place(x=300, y=110)

asd = tk.Label(root, text='Навигация', background='#1e2329', fg='#c4cacf',
               font=('', 13))
asd.place(x=10, y=62)

df = PhotoImage(file='frame12.png')
df = df.subsample(6)
ass = tk.Label(root, image=df, background='#1e2329')
ass.place(x=10, y=120)
hghg = tk.Label(root, text='Главная', font=('', 14), background='#1e2329',
                fg='#c4cacf')
hghg.place(x=65, y=130)
hghg.bind('<Button-1>', open_main_str)

dfd = PhotoImage(file='frame13.png')
dfd = dfd.subsample(6)
asff = tk.Label(root, image=dfd, background='#1e2329')
asff.place(x=10, y=180)
hghgg = tk.Label(root, text='Монитор ТА', font=('', 14), background='#1e2329',
                 fg='#c4cacf')
hghgg.place(x=65, y=190)
hghgg.bind('<Button-1>', open_monik_str)

aaa = PhotoImage(file='frame14.png')
aaa = aaa.subsample(6)
asas = tk.Label(root, image=aaa, background='#1e2329')
asas.place(x=10, y=240)
hghhg = tk.Label(root, text='Детальные отчеты', font=('', 14),
                 background='#1e2329',
                 fg='#c4cacf')
hghhg.place(x=65, y=250)
hghhg.bind('<Button-1>', open_pod_menu_detot)

ggg = PhotoImage(file='frame16.png')
ggg = ggg.subsample(6)
lkj = tk.Label(root, image=ggg, background='#1e2329')
lkj.place(x=10, y=300)
hhhhg = tk.Label(root, text='Учет ТМЦ', font=('', 14), background='#1e2329',
                 fg='#c4cacf')
hhhhg.place(x=65, y=310)
hhhhg.bind('<Button-1>', open_pod_menu_ychet)

ddd = PhotoImage(file='frame15.png')
ddd = ddd.subsample(6)
sdf = tk.Label(root, image=ddd, background='#1e2329')
sdf.place(x=10, y=360)
hhhhh = tk.Label(root, text='Администрирование', font=('', 14),
                 background='#1e2329',
                 fg='#c4cacf')
hhhhh.place(x=65, y=370)
hhhhh.bind('<Button-1>', open_pod_menu_admin)

galka = PhotoImage(file='galka.png')
galka = galka.subsample(10)

soss = PhotoImage(file='menuk.png')
soss = soss.subsample(10)

ff1 = tk.Label(root, image=galka, background='#1e2329')
ff1.place(x=250, y=250)
ff1.bind('<Button-1>', close_pod_menu_detot)
ff2 = tk.Label(root, image=galka, background='#1e2329')
ff2.place(x=250, y=310)
ff2.bind('<Button-1>', close_pod_menu_ychet)
ff3 = tk.Label(root, image=galka, background='#1e2329')
ff3.place(x=250, y=370)
ff3.bind('<Button-1>', close_pod_menu_adnim)

root.mainloop()
