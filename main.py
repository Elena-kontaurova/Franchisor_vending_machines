''' api '''
from fastapi import FastAPI, Request
from connect import VendingMachine, Product, Sale, User, Maintenance, \
    Torfavt, Kompany, Soston_svz, Zagrux, Denech_sredst, Inform_Status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI() # бл

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/', response_class=HTMLResponse)
async def main_str(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})


@app.get('/torg', response_class=HTMLResponse)
async def torg_str(request: Request):
    torg_avt = Torfavt.select()
    avtom = [{
        'id': avt.id,
        'name': avt.name,
        'model': avt.model,
        'kompany': avt.kompany,
        'modem': avt.modem,
        'adress': avt.adress,
        'word': avt.word,
        'deist': avt.deist,
        
    } for avt in torg_avt]
    return templates.TemplateResponse('torg.html',
                                      {'request': request,
                                       'torg_avt': avtom})


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


@app.get('/torg/{torg_avt_id}')
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


@app.get('/comp/{copm_id}')
async def get_id_comp(copm_id):
    comp = Kompany.get(Kompany.id == copm_id)
    return {
        'id': comp.id,
        'name': comp.name,
        'veshe': comp.veshe,
        'adres': comp.adres,
        'kontak': comp.kontak,
        'work': comp.work,
        'deist': comp.deist,
        'prim': comp.prim
    }


@app.get('/comp')
async def get_comp():
    com = Kompany.select()
    return [{
        'id': comp.id,
        'name': comp.name,
        'veshe': comp.veshe,
        'adres': comp.adres,
        'kontak': comp.kontak,
        'work': comp.work,
        'deist': comp.deist,
        'prim': comp.prim
    }
     for comp in com]


@app.get('/sostoinie')
async def get_sost():
    sost = Soston_svz.select()
    return [{
        'id': sos.id,
        'comp': sos.comp,
        'pay': sos.pay,
        'time': sos.time
    } for sos in sost]


@app.get('/zagruz')
async def get_zagruz():
    zagr = Zagrux.select()
    return [{
        'id': zag.id,
        'base': zag.base,
        'minim': zag.minim
    } for zag in zagr]


@app.get('/denech')
async def get_denech():
    dene = Denech_sredst.select()
    return [{
        'id': den.id,
        'one_den': den.one_den,
        'two_den': den.two_den,
        'three_den': den.three_den
    } for den in dene]


@app.get('/inform')
async def get_inform():
    info = Inform_Status.select()
    return [{
        'id': inf.id,
        'podk': inf.podk,
        'nastr': inf.nastr,
        'oblak': inf.oblak
    } for inf in info]

# устала ужее
