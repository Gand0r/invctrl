from pydantic import BaseModel

class StokBarang(BaseModel):
    nama_barang: str
    jumlah: int
