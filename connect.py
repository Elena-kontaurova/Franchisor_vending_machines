''' бд'''
from peewee import Model, MySQLDatabase, AutoField, IntegerField, \
                    CharField, DateField, DateTimeField, FloatField, \
                    ForeignKeyField

db = MySQLDatabase('franprof', user='root', password='lenok',
                   host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


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


db.connect()
db.create_tables([VendingMachine, Product, Sale,
                  User, Maintenance, Svodka, News,
                  Torfavt, Kompany, Soston_svz,
                  Zagrux, Denech_sredst, Inform_Status], safe=True)
db.close()
