# InvCtrl

**InvCtrl** (Inventory Control) adalah aplikasi web berbasis FastAPI untuk kebutuhan manajemen inventaris seperti permintaan barang dari toko/karyawan, pengelolaan stok, dan tampilan dashboard sederhana.

---

## Persyaratan

- Python 3.8 atau lebih baru  
- Internet connection (untuk install package dari PyPI)

---

## Cara Instalasi & Menjalankan Aplikasi

### 1. Install Python

Unduh dan install Python dari [https://www.python.org/downloads/](https://www.python.org/downloads/)

Pastikan saat install:
- Checklist **"Add Python to PATH"**
- Setelah selesai, cek versi:
  ```bash
  python --version

- Buat Virtual Environment
  ```python -m venv venv```

- Aktifkan environment:
  
  Windows
  ```
  venv\Scripts\activate
  ```
  
  Linux/MacOS
  ```
  source venv/bin/activate
  ```
  
### 2. Install InvCtrl dari PyPI
  ```
  pip install invctrl
  ```
    

### 3. Jalankan Aplikasi
  ```
  invctrl
  ```

### 4. Install via Github

- Clone Repository
```
git clone https://github.com/Gand0r/invctrl.git
```
- Masuk ke directory
```
cd invctrl
```
- Lalu Jalankan
```
run_app.bat
```
Aplikasi berjalan di http://localhost:8000/dashboard

---

## 5. Fitur
  - Form permintaan barang
  - Penyimpanan menggunakan TinyDB (NoSQL, ringan, berbasis file)
  - Template HTML dengan Jinja2
  - Routing modular (FastAPI)
  - CLI command siap pakai: invctrl

---

## SCREENSHOOT

### 1. Tampilan Request Order
![Tampilan Request Order](https://raw.githubusercontent.com/Gand0r/invctrl/main/img/Tampilan%20RO.PNG)

### 2. Tampilan Purchase Order
![Tampilan Purchase Order](https://raw.githubusercontent.com/Gand0r/invctrl/main/img/Tampilan%20PO.PNG)

### 3. Tampilan Stock Barang
![Tampilan Purchase Order](https://raw.githubusercontent.com/Gand0r/invctrl/main/img/Tampilan%20Stock.PNG)

### 4. Tampilan Delivery Order
![Tampilan Purchase Order](https://raw.githubusercontent.com/Gand0r/invctrl/main/img/Tampilan%20DO.PNG)
