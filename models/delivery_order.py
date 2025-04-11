from pydantic import BaseModel

class DeliveryOrder(BaseModel):
    nama_barang: str
    jumlah: int
    tujuan: str
