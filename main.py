from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB
from routes import request_order

app = FastAPI()
templates = Jinja2Templates(directory="templates")

request_db = TinyDB("db/request_order.json")

@app.get("/dashboard")
def dashboard(request: Request):
    data = request_db.all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})

@app.post("/request-order")
def handle_form(
    nama_barang: str = Form(...),
    jumlah: int = Form(...),
    nama_toko: str = Form(...)
):
    request_db.insert({
        "nama_barang": nama_barang,
        "jumlah": jumlah,
        "nama_toko": nama_toko
    })
    return RedirectResponse(url="/dashboard", status_code=303)

app.include_router(request_order.router)
