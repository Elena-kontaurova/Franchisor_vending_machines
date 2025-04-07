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


db.connect()
db.create_tables([VendingMachine, Product, Sale,
                  User, Maintenance, Svodka], safe=True)
db.close()
