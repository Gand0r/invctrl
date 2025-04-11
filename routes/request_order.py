from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.request_order import RequestOrder, PurchaseOrder
from models.stock import StokBarang
from models.delivery_order import DeliveryOrder
from utils.file_db import load_json, save_json


templates = Jinja2Templates(directory="templates")
router = APIRouter()

request_orders = []
purchase_orders = []
stok_barang = []
delivery_orders = []


PO_FILE = "data/purchase_orders.json"
STOK_FILE = "data/stock_barang.json"
DO_FILE = "data/delivery_orders.json"

purchase_orders = [PurchaseOrder(**item) for item in load_json(PO_FILE)]
stok_barang = [StokBarang(**item) for item in load_json(STOK_FILE)]
delivery_orders = [DeliveryOrder(**item) for item in load_json(DO_FILE)]


@router.get("/dashboard")
def show_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": request_orders})

@router.post("/request-order")
def create_ro(nama_barang: str = Form(...), jumlah: int = Form(...), nama_toko: str = Form(...)):
    ro = RequestOrder(nama_barang=nama_barang, jumlah=jumlah, nama_toko=nama_toko)
    request_orders.append(ro)
    return RedirectResponse("/dashboard", status_code=302)

@router.post("/create-po")
def create_po(nama_barang: str = Form(...), jumlah: int = Form(...), nama_toko: str = Form(...)):
    po = PurchaseOrder(nama_barang=nama_barang, jumlah=jumlah, nama_toko=nama_toko)
    purchase_orders.append(po)
    save_json(PO_FILE, [item.dict() for item in purchase_orders])
    return RedirectResponse("/purchase-orders", status_code=302)


@router.get("/purchase-orders")
def list_po(request: Request):
    return templates.TemplateResponse("purchase_orders.html", {"request": request, "po_data": purchase_orders})

@router.post("/stock-in")
def stock_in(nama_barang: str = Form(...), jumlah: int = Form(...), index: int = Form(...)):
    if index < len(purchase_orders):
        purchase_orders[index].status = "Received"
        save_json(PO_FILE, [item.dict() for item in purchase_orders])

    for item in stok_barang:
        if item.nama_barang == nama_barang:
            item.jumlah += jumlah
            break
    else:
        stok_barang.append(StokBarang(nama_barang=nama_barang, jumlah=jumlah))

    save_json(STOK_FILE, [item.dict() for item in stok_barang])

    return RedirectResponse("/purchase-orders", status_code=302)


@router.get("/stock")
def lihat_stok(request: Request):
    return templates.TemplateResponse("stock.html", {
        "request": request,
        "stok": stok_barang
    })

@router.get("/delivery-order")
def form_do(request: Request):
    return templates.TemplateResponse("delivery_order.html", {
        "request": request,
        "stok": stok_barang,
        "data": delivery_orders
    })

@router.post("/delivery-order")
def create_do(nama_barang: str = Form(...), jumlah: int = Form(...), tujuan: str = Form(...)):
    for item in stok_barang:
        if item.nama_barang == nama_barang:
            if item.jumlah >= jumlah:
                item.jumlah -= jumlah
                do = DeliveryOrder(nama_barang=nama_barang, jumlah=jumlah, tujuan=tujuan)
                delivery_orders.append(do)
                save_json(STOK_FILE, [item.dict() for item in stok_barang])
                save_json(DO_FILE, [item.dict() for item in delivery_orders])
                break
            else:
                return RedirectResponse("/delivery-order?error=stok_kurang", status_code=302)
    else:
        return RedirectResponse("/delivery-order?error=tidak_ada_barang", status_code=302)

    return RedirectResponse("/delivery-order", status_code=302)
 