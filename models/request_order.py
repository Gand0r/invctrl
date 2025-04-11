from pydantic import BaseModel

class RequestOrder(BaseModel):
    nama_barang: str
    jumlah: int
    nama_toko: str

class PurchaseOrder(BaseModel):
    nama_barang: str
    jumlah: int
    nama_toko: str
    status: str = "Waiting"

class StokBarang(BaseModel):
    nama_barang: str
    jumlah: int