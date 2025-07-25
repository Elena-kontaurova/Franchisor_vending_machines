''' бд'''
from peewee import Model, MySQLDatabase, AutoField, IntegerField, \
                    CharField, DateField, DateTimeField, FloatField, \
                    ForeignKeyField

db = MySQLDatabase('franprof', user='root', password='lenok',
                   host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


# ао
class VendingMachine(BaseModel):
    id = AutoField()
    location = CharField()
    model = CharField()
    type_machine = CharField(choices=[('cash', 'Оплата наличными'),
                                      ('card', 'Оплата картой'),
                                      ('both', 'Оба способа')])
    status = CharField(choices=[('working', 'рабочий'),
                                ('not_workint', 'не рабочий'),
                                ('maintenance', 'на обслуживании')])
    installation_date = DateField()
    last_service_date = DateField()
    total_income = IntegerField()


class Product(BaseModel):
    id = AutoField()
    name = CharField()
    description = CharField()
    price = IntegerField()
    quantity_in_stock = IntegerField()
    minimum_stock = IntegerField()
    sales_trend = FloatField()


class Sale(BaseModel):
    id = AutoField()
    vending_machine = ForeignKeyField(VendingMachine, backref='sales')
    product = ForeignKeyField(Product, backref='sales')
    quantity = IntegerField()
    total_amount = IntegerField()
    sale_datetime = DateTimeField()
    payment_method = CharField(choices=[('cash', 'наличные'),
                                        ('card', 'карта'),
                                        ('qr', 'QR')])


class User(BaseModel):
    id = AutoField()
    full_name = CharField()
    email = CharField()
    phone = CharField()
    role = CharField(choices=[('admin', 'администратор',
                               'operator', 'оператор')])


class Maintenance(BaseModel):
    id = AutoField()
    vending_machine = ForeignKeyField(VendingMachine, backref='maintences')
    maintenance_date = DateField()
    work_description = CharField()
    problems = CharField()
    executor = CharField()


class Svodka(BaseModel):
    id = AutoField()
    name = CharField()
    price = CharField()


class News(BaseModel):
    id = AutoField()
    date = CharField()
    text = CharField()


class Torfavt(BaseModel):
    id = AutoField()
    name = CharField()
    model = CharField()
    kompany = CharField()
    modem = CharField()
    adress = CharField()
    word = CharField()
    deist = CharField()


class Kompany(BaseModel):
    id = AutoField()
    name = CharField()
    veshe = CharField()
    adres = CharField()
    kontak = CharField()
    work = CharField()
    deist = CharField(null=True)
    prim = CharField()


class Soston_svz(BaseModel):
    id = AutoField()
    comp = CharField()
    pay = CharField()
    time = CharField()


class Zagrux(BaseModel):
    id = AutoField()
    base = CharField()
    minim = CharField()


class Denech_sredst(BaseModel):
    id = AutoField()
    one_den = CharField()
    two_den = CharField()
    three_den = CharField()


class Inform_Status(BaseModel):
    id = AutoField()
    podk = CharField()
    nastr = CharField()
    oblak = CharField()


class AutorizRegus(BaseModel):
    id = AutoField()
    user = CharField()
    password = CharField()
    role = CharField()


class Otchet_torgov_avtomat(BaseModel):
    id = AutoField()
    itigo_avtomatov = IntegerField()
    uspolzuen = CharField()
    svobodno = CharField()
    rabotaet = CharField()
    ne_rabotaey = CharField()
    trebue_obsluch = CharField()
    provetka = CharField()


class Otchet_monitor(BaseModel):
    id = AutoField()
    itogo_avtomatov = CharField()
    rabotaut = CharField()
    repairs_are_pending = CharField()
    uroven_sred = CharField()  # средний уровень загрузки
    ob_verch = CharField()  # общая выручка
    zamenu = CharField()
    new_oborud = CharField()
    monitor = CharField()


class Otchet_kompanyu(BaseModel):
    id = AutoField()
    itigo_kompanu = CharField()
    deqist = CharField()
    sotrud = CharField()
    naluch_avtom = CharField()  # наличие авттоматов


class Forma_str1(BaseModel):
    id = AutoField()
    data_zac = CharField()
    data_doc = CharField()
    kol_vo = CharField()


class Forma_str2(BaseModel):
    id = AutoField()
    data_zac = CharField()
    data_doc = CharField()
    kol_vo = CharField()


class Forma_str3(BaseModel):
    id = AutoField()
    data_zac = CharField()
    data_doc = CharField()
    kol_vo = CharField()


class Polzovat(BaseModel):
    id = AutoField()
    name = CharField()
    naznach = CharField()


class Modem(BaseModel):
    id = AutoField()
    model = CharField()
    wifi = CharField()
    iter = CharField()
    strana = CharField()


class Dop(BaseModel):
    id = AutoField()
    name_l = CharField()
    last = CharField()
    name_r = CharField()
    rel = CharField()


class Profile_user(BaseModel):
    id = AutoField()
    user_id = ForeignKeyField(AutorizRegus)
    tg = CharField(null=True)
    vk = CharField(null=True)
    github = CharField(null=True)
    web = CharField(null=True)
    full_name = CharField(null=True)
    email = CharField(null=True)
    phone = CharField(null=True)
    adress = CharField(null=True)


class Monitor_TA(BaseModel):
    id = AutoField()
    name = CharField()
    connection_status = CharField()  # Статус связи
    last_connection = IntegerField()  # Время с последней связи в минутах
    load_percent = IntegerField()    # Процент загрузки
    money_amount = IntegerField()    # Денежные средства
    events = CharField()             # События
    location = CharField()           # Местоположение


db.connect()
db.create_tables([VendingMachine, Product, Sale,
                  User, Maintenance, Svodka, News,
                  Torfavt, Kompany, Soston_svz,
                  Zagrux, Denech_sredst, Inform_Status,
                  AutorizRegus, Otchet_torgov_avtomat,
                  Otchet_monitor, Otchet_kompanyu,
                  Forma_str1, Forma_str2, Forma_str3,
                  Modem, Dop, Profile_user, Monitor_TA],
                 safe=True)
db.close()
