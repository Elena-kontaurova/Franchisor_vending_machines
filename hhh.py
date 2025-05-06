''' api '''
from fastapi import FastAPI, Request
from connect import VendingMachine, Product, Sale, User, Maintenance, Torfavt
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', response_class=HTMLResponse)
async def main_str(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})

@app.get('/torg', response_class=HTMLResponse)
async def torg_str(request: Request):
    return templates.TemplateResponse('torg.html',
                                      {'request': request})


@app.get('/dogo', response_class=HTMLResponse)
async def dogo_str(request: Request):
    return templates.TemplateResponse('dogo.html',
                                      {'request': request})


@app.get('/nast', response_class=HTMLResponse)
async def nast_str(request: Request):
    return templates.TemplateResponse('nast.html',
                                      {'request': request})


@app.get('/vendi')
async def get_vending_machine():
    vendi = VendingMachine.select()
    return [{'id': ven.id,
             'location': ven.location,
             'model': ven.model,
             'type_machine': ven.type_machine,
             'status': ven.status,
             'installation_date': ven.installation_date,
             'last_service_date': ven.last_service_date,
             'total_income': ven.total_income}
            for ven in vendi]


@app.get('/product')
async def get_product():
    prod = Product.select()
    return [{'id': pro.id,
             'name': pro.name,
             'description': pro.description,
             'price': pro.price,
             'quantity_in_stock': pro.quantity_in_stock,
             'minimum_stock': pro.minimum_stock,
             'sales_trend': pro.sales_trend}
            for pro in prod]


@app.get('/sale')
async def get_sale():
    sale = Sale.select()
    return [{'id': se.id,
             'vending_machine': se.vending_machine,
             'product': se.product,
             'quantity': se.quantity,
             'total_amount': se.total_amount,
             'sale_datetime': se.sale_datetime,
             'payment_method': se.payment_method}
            for se in sale]


@app.get('/user')
async def get_user():
    user = User.select()
    return [{'id': us.id,
             'full_name': us.full_name,
             'email': us.email,
             'phone': us.phone,
             'role': us.role}
            for us in user]


@app.get('/mainte')
async def get_mainte():
    mainte = Maintenance.select()
    return [{'id': ma.id,
             'vending_machine': ma.vending_machine,
             'maintenance_date': ma.maintenance_date,
             'work_description': ma.work_description,
             'problems': ma.problems,
             'executor': ma.executor}
            for ma in mainte]


@app.get('/torgi/{torg_avt_id}')
async def get_id_torg(torg_avt_id):
    torg_avt = Torfavt.get(Torfavt.id == torg_avt_id)
    return {
        'id': torg_avt.id,
        'name': torg_avt.name,
        'model': torg_avt.model,
        'kompany': torg_avt.kompany,
        'modem': torg_avt.modem,
        'adress': torg_avt.adress,
        'word': torg_avt.word,
        'deist': torg_avt.deist,
    }

 # эм
