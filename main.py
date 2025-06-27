''' api '''
from fastapi import FastAPI, Request
from connect import VendingMachine, Product, Sale, User, Maintenance, \
    Torfavt, Kompany, Soston_svz, Zagrux, Denech_sredst, Inform_Status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND

app = FastAPI()  # бл

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == HTTP_404_NOT_FOUND:
        return templates.TemplateResponse(
            "error404.html",
            {"request": request},
            status_code=HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        {"detail": exc.detail},
        status_code=exc.status_code
    )


@app.get('/404', response_class=HTMLResponse)
async def error_404(request: Request):
    return templates.TemplateResponse('error404.html',
                                      {'request': request})


@app.get('/', response_class=HTMLResponse)
async def main_str(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request})


@app.get('/monitor', response_class=HTMLResponse)
async def monik_str(request: Request):
    return templates.TemplateResponse('monitor.html',
                                      {'request': request})


@app.get('/sales', response_class=HTMLResponse)
async def torg_str(request: Request):
    return templates.TemplateResponse('otch_torgavt.html',
                                      {'request': request})


@app.get('/stock', response_class=HTMLResponse)
async def torg_stock(request: Request):
    return templates.TemplateResponse('otch_monik.html',
                                      {'request': request})


@app.get('/movements', response_class=HTMLResponse)
async def torg_movements(request: Request):
    return templates.TemplateResponse('otch_kompany.html',
                                      {'request': request})


@app.get('/water', response_class=HTMLResponse)
async def ychet_water(request: Request):
    return templates.TemplateResponse('apparat_water.html',
                                      {'request': request})


@app.get('/sweet', response_class=HTMLResponse)
async def ychet_sweeet(request: Request):
    return templates.TemplateResponse('apparat_sweet.html',
                                      {'request': request})


@app.get('/snacks', response_class=HTMLResponse)
async def ychet_snacks(request: Request):
    return templates.TemplateResponse('apparat_snacks.html',
                                      {'request': request})


@app.get('/torgavt', response_class=HTMLResponse)
async def adm_torgavt(request: Request):
    return templates.TemplateResponse('adm_torgavt.html',
                                      {'request': request})


@app.get('/company', response_class=HTMLResponse)
async def adm_company(request: Request):
    return templates.TemplateResponse('adm_company.html',
                                      {'request': request})


@app.get('/polsivat', response_class=HTMLResponse)
async def adm_polsovat(request: Request):
    return templates.TemplateResponse('adm_polsovat.html',
                                      {'request': request})


@app.get('/modem', response_class=HTMLResponse)
async def adm_modem(request: Request):
    return templates.TemplateResponse('adm_modem.html',
                                      {'request': request})


@app.get('/dop', response_class=HTMLResponse)
async def adm_dop(request: Request):
    return templates.TemplateResponse('adm_dop.html',
                                      {'request': request})


@app.get('/products', response_class=HTMLResponse)
async def adm_products(request: Request):
    return templates.TemplateResponse('product.html',
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
