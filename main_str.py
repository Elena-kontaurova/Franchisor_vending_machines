import tkinter as tk
from tkinter import PhotoImage, messagebox
from connect import Svodka, News, Torfavt, Kompany


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


def get_tor():
    torg = Torfavt.select()
    return torg


def get_komp():
    kom = Kompany.select()
    return kom


def open_torg_avt(_):
    ''' Администрирование / торговые автоматы'''

    def create_zap():
        ff = tk.Toplevel()
        ff.geometry('300x500')
        ff.title('Создание торгового автомата')

        la = tk.Label(ff, background='#c4cacf', width=300, height=3)
        la.place(x=0, y=0)
        oglav = tk.Label(ff, text='Создание торгового аппарата',
                         font=('', 15), fg='#1489cc', background='#c4cacf')
        oglav.place(x=10, y=10)

        name = tk.Label(ff, text='Название автомата:')
        name.place(x=20, y=60)
        name1 = tk.Entry(ff)
        name1.place(x=140, y=60)

        model = tk.Label(ff, text='Модель:')
        model.place(x=20, y=90)
        m = tk.Entry(ff)
        m.place(x=140, y=90)

        kompany = tk.Label(ff, text='Компания:')
        kompany.place(x=20, y=120)
        k = tk.Entry(ff)
        k.place(x=140, y=120)

        modem = tk.Label(ff, text='Модем:')
        modem.place(x=20, y=150)
        m1 = tk.Entry(ff)
        m1.place(x=140, y=150)

        adress = tk.Label(ff, text='Адерес/Место:')
        adress.place(x=20, y=180)
        a = tk.Entry(ff)
        a.place(x=140, y=180)

        word = tk.Label(ff, text='В работе с:')
        word.place(x=20, y=210)
        w = tk.Entry(ff)
        w.place(x=140, y=210)

        deist = tk.Label(ff, text='Действия:')
        deist.place(x=20, y=240)
        d = tk.Entry(ff)
        d.place(x=140, y=240)

        def gr_zz():
            name = name1.get()
            model = m.get()
            kompany = k.get()
            modem = m1.get()
            adress = a.get()
            word = w.get()
            deist = d.get()

            _ = Torfavt.create(
                name=name,
                model=model,
                kompany=kompany,
                modem=modem,
                adress=adress,
                word=word,
                deist=deist
            )
            messagebox.showinfo('Успех', 'Запись успещно создана')
            ff.destroy()

        cre = tk.Button(ff, text='Создать', background='#1489cc',
                        width=13, fg='white', command=gr_zz)
        cre.place(x=20, y=280)

        ff.mainloop()

    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Торговые автоматы',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=800, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)
    kvad = tk.Label(hh, width=100, height=34, background='white')
    kvad.place(x=70, y=30)
    hh = tk.Label(kvad, background='#ededed', width=100, height=3)
    hh.place(x=0, y=0)
    tt = tk.Label(hh, text='Торговые автоматы', background='#ededed',
                  fg='#1489cc', font=('', 12))
    tt.place(x=10, y=5)
    df = tk.Label(hh, text='Всего найдено 9 записей', background='#ededed',
                  fg='black', font=('', 7))
    df.place(x=12, y=25)
    kn_create = tk.Button(hh, text='Добавить', background='#ededed',
                          fg='black', command=create_zap)
    kn_create.place(x=610, y=15)

    table = tk.Label(kvad, width=97, height=29, background='#adb4b8')
    table.place(x=10, y=60)
    t_1 = tk.Label(table,
                   text='ID', background='#adb4b8')
    t_1.place(x=30, y=10)
    t_2 = tk.Label(table,
                   text='Навазание \n автомата',
                   background='#adb4b8')
    t_2.place(x=90, y=5)
    t_3 = tk.Label(table, text='Модель', background='#adb4b8')
    t_3.place(x=190, y=10)
    t_4 = tk.Label(table, text='Компания', background='#adb4b8')
    t_4.place(x=270, y=10)
    t_5 = tk.Label(table, text='Модем', background='#adb4b8')
    t_5.place(x=360, y=10)
    t_6 = tk.Label(table, text='Адресс/Место', background='#adb4b8')
    t_6.place(x=430, y=10)
    t_7 = tk.Label(table, text='В работе \n с', background='#adb4b8')
    t_7.place(x=530, y=5)
    t_8 = tk.Label(table, text='Действия', background='#adb4b8')
    t_8.place(x=600, y=10)

    def update_torg_avt(item, name, model, kompany, modem, adress, word):
        aga = Torfavt.get(Torfavt.id == item.id)
        aga.name = name
        aga.model = model
        aga.kompany = kompany
        aga.modem = modem
        aga.adress = adress
        aga.word = word
        aga.save()

    def redak_torg_avt(item):
        mm = tk.Toplevel()
        mm.geometry('500x300')
        mm.title('Редактирование торгового автомата')

        a = tk.Label(mm, text='Название автомата:')
        a.place(x=20, y=20)
        name = tk.Entry(mm)
        name.insert(0, item.name)
        name.place(x=20, y=45)

        b = tk.Label(mm, text='Модель:')
        b.place(x=180, y=20)

        model = tk.Entry(mm)
        model.insert(0, item.model)
        model.place(x=180, y=45)

        c = tk.Label(mm, text='Компания:')
        c.place(x=20, y=85)

        komp = tk.Entry(mm, width=40)
        komp.insert(0, item.kompany)
        komp.place(x=20, y=110)

        d = tk.Label(mm, text='Модем:')
        d.place(x=280, y=85)

        modem = tk.Entry(mm)
        modem.insert(0, item.modem)
        modem.place(x=280, y=110)

        e = tk.Label(mm, text='Адресс/Место:')
        e.place(x=20, y=145)

        adress = tk.Entry(mm, width=30)
        adress.insert(0, item.adress)
        adress.place(x=20, y=170)

        f = tk.Label(mm, text='В работе с')
        f.place(x=230, y=145)

        word = tk.Entry(mm)
        word.insert(0, item.word)
        word.place(x=230, y=170)

        kn = tk.Label(mm, text='Сохранить', width=25,
                      background='#1489CC', fg='white')

        kn = tk.Button(mm, text='Сохранить', width=25,
                       background='#1489CC', fg='white')
        kn.place(x=20, y=220)

        def update_info():
            new_name = name.get()
            new_model = model.get()
            new_komp = komp.get()
            new_modem = modem.get()
            new_adress = adress.get()
            new_word = word.get()
            update_torg_avt(item, new_name, new_model, new_komp,
                            new_modem, new_adress, new_word)

            messagebox.showinfo("Успех", "Данные успешно сохранены!")
            mm.destroy()

        kn.config(command=update_info)

        mm.mainloop()

    def delete_torg_avt(item):
        mm = tk.Toplevel()
        mm.geometry('250x100')
        mm.title('Удаление торгового автомата')

        def del_zap():
            Torfavt.delete().where(Torfavt.id == item.id).execute()
            messagebox.showinfo('Успех', 'Данные успешно удаленны')
            mm.destroy()

        def del_fram():
            mm.destroy()

        a = tk.Label(mm, text='Вы действительно хотите удалить запись?')
        a.place(x=10, y=10)
        yes = tk.Button(mm, text='Да', background='#f00c36', fg='white',
                        width=13, command=del_zap)
        yes.place(x=10, y=50)
        no = tk.Button(mm, text='Нет', background='#0c14f0', fg='white',
                       width=13, command=del_fram)
        no.place(x=140, y=50)
        mm.mainloop()

    torg = get_tor()
    lox = 50
    for i in torg:
        asas = '#d9dadb'
        if i.id % 2 == 0:
            asas = '#ededed'
        dfd = tk.Label(table, width=97, height=2, background=asas)
        dfd.place(x=0, y=lox)
        lox += 40
        h_1 = tk.Label(dfd, text=f'{i.id}', background=asas)
        h_1.place(x=30, y=5)
        h_2 = tk.Label(dfd, text=f'{i.name}', background=asas,
                       wraplength=90, justify='center', fg='#1489CC')
        h_2.place(x=100, y=5)
        h_3 = tk.Label(dfd, text=f'{i.model}', background=asas,
                       wraplength=70, justify='center', font=('', 8))
        h_3.place(x=190, y=0)
        h_4 = tk.Label(dfd, text=f'{i.kompany}', background=asas,
                       wraplength=80, justify='center', font=('', 6),
                       fg='#1489CC')
        h_4.place(x=260, y=0)
        h_5 = tk.Label(dfd, text=f'{i.modem}', background=asas)
        h_5.place(x=350, y=5)
        h_6 = tk.Label(dfd, text=f'{i.adress}', background=asas,
                       wraplength=70, justify='center', font=('', 8))
        h_6.place(x=440, y=0)
        h_7 = tk.Label(dfd, text=f'{i.word}', background=asas)
        h_7.place(x=530, y=5)
        h_8 = tk.Label(dfd, text='R', background=asas,
                       fg='#1489CC')
        h_8.place(x=610, y=5)
        h_8.bind('<Button-1>', lambda event, item=i: redak_torg_avt(item))

        h_9 = tk.Label(dfd, text='D', background=asas,
                       fg='#1489CC')
        h_9.place(x=630, y=5)
        h_9.bind('<Button-1>', lambda event, item=i: delete_torg_avt(item))

        h_0 = tk.Label(dfd, text='C', background=asas,
                       fg='#1489CC')
        h_0.place(x=650, y=5)


def open_komp(_):
    ''' Администрирование / Компании '''

    def create_komp():
        mm = tk.Toplevel()
        mm.geometry('500x300')
        mm.title('Создание компании')

    ff = tk.Label(root, background='#060a0d', width=100, height=10)
    ff.place(x=800, y=50)
    gg = tk.Label(root, text='Администирование / Компании',
                  background='#060a0d', fg='#c4cacf',
                  font=('', 12))
    gg.place(x=870, y=60)
    hh = tk.Label(root, width=200, height=200,
                  background='#c4cacf')
    hh.place(x=285, y=100)
    kvad = tk.Label(hh, width=100, height=34, background='white')
    kvad.place(x=70, y=30)
    hh = tk.Label(kvad, background='#ededed', width=100, height=3)
    hh.place(x=0, y=0)
    tt = tk.Label(hh, text='Cписок компаний', background='#ededed',
                  fg='#1489cc', font=('', 12))
    tt.place(x=10, y=5)
    df = tk.Label(hh, text='Всего найдено 9 записей', background='#ededed',
                  fg='black', font=('', 7))
    df.place(x=12, y=25)
    kn_create = tk.Button(hh, text='Добавить', background='#ededed',
                          fg='black', command=create_komp)
    kn_create.place(x=610, y=15)

    table = tk.Label(kvad, width=97, height=29, background='#adb4b8')
    table.place(x=10, y=60)
    t_2 = tk.Label(table,
                   text='Навазание',
                   background='#adb4b8')
    t_2.place(x=40, y=10)
    t_3 = tk.Label(table, text='Вышестоящая', background='#adb4b8')
    t_3.place(x=150, y=10)
    t_4 = tk.Label(table, text='Адрес', background='#adb4b8')
    t_4.place(x=290, y=10)
    t_5 = tk.Label(table, text='Контакты', background='#adb4b8')
    t_5.place(x=370, y=10)
    t_6 = tk.Label(table, text='В работе с', background='#adb4b8')
    t_6.place(x=460, y=10)
    t_7 = tk.Label(table, text='Действия', background='#adb4b8')
    t_7.place(x=560, y=10)

    def update_komp(item):
        mm = tk.Toplevel()
        mm.geometry('500x200')
        mm.title('Редактирование компании')

        a = tk.Label(mm, text='Название:')
        a.place(x=10, y=10)
        f1 = tk.Entry(mm)
        f1.insert(0, item.name)
        f1.place(x=10, y=35)

        b = tk.Label(mm, text='Вышестоящие:')
        b.place(x=160, y=10)
        f6 = tk.Entry(mm)
        f6.insert(0, item.veshe)
        f6.place(x=160, y=35)

        c = tk.Label(mm, text='Адресс:')
        c.place(x=310, y=10)
        f2 = tk.Entry(mm)
        f2.insert(0, item.adres)
        f2.place(x=310, y=35)

        d = tk.Label(mm, text='Контакты:')
        d.place(x=10, y=70)
        f3 = tk.Entry(mm)
        f3.insert(0, item.kontak)
        f3.place(x=10, y=95)

        e = tk.Label(mm, text='В работе с:')
        e.place(x=160, y=70)
        f4 = tk.Entry(mm)
        f4.insert(0, item.work)
        f4.place(x=160, y=95)

        kn = tk.Button(mm, text='Сохранить', width=20,
                       background='#1489CC', fg='white')
        kn.place(x=10, y=140)

    def del_komp(item):
        mm = tk.Toplevel()
        mm.geometry('300x300')
        mm.title('Удаление компании')

    kom = get_komp()
    lox = 50
    for i in kom:
        asas = '#d9dadb'
        if i.id % 2 == 0:
            asas = '#ededed'
        dfd = tk.Label(table, width=97, height=2, background=asas)
        dfd.place(x=0, y=lox)
        lox += 40

        h_2 = tk.Label(dfd, text=f'{i.name}', background=asas,
                       wraplength=90, justify='center', fg='#1489CC')
        h_2.place(x=40, y=0)

        h_3 = tk.Label(dfd, text=f'{i.veshe}', background=asas,
                       wraplength=70, justify='center', font=('', 7))
        h_3.place(x=160, y=0)

        h_4 = tk.Label(dfd, text=f'{i.adres}', background=asas,
                       wraplength=80, justify='center', font=('', 9),
                       fg='#1489CC')
        h_4.place(x=280, y=0)

        h_5 = tk.Label(dfd, text=f'{i.kontak}', background=asas)
        h_5.place(x=370, y=5)

        h_6 = tk.Label(dfd, text=f'{i.work}', background=asas,
                       wraplength=70, justify='center', font=('', 10))
        h_6.place(x=460, y=5)

        h_8 = tk.Label(dfd, text='R', background=asas,
                       fg='#1489CC')
        h_8.place(x=580, y=5)
        h_8.bind('<Button-1>', lambda event, item=i: update_komp(item))

        h_9 = tk.Label(dfd, text='D', background=asas,
                       fg='#1489CC')
        h_9.place(x=600, y=5)
        h_9.bind('<Button-1>', lambda event, item=i: del_komp(item))

        h_0 = tk.Label(dfd, text='C', background=asas,
                       fg='#1489CC')
        h_0.place(x=620, y=5)


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
