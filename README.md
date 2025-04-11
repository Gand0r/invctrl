# InvCtrl

**InvCtrl** adalah aplikasi web berbasis FastAPI untuk kebutuhan manajemen inventaris seperti permintaan barang dari toko/karyawan, pengelolaan stok, dan tampilan dashboard sederhana.

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
```
git clone https://github.com/Gand0r/invctrl.git
```
masuk ke directory
```
cd invctrl
```
jalankan run_app.bat

Aplikasi berjalan di http://localhost:8000/dashboard

---

## 4. Fitur
  - Form permintaan barang
  - Penyimpanan menggunakan TinyDB (NoSQL, ringan, berbasis file)
  - Template HTML dengan Jinja2
  - Routing modular (FastAPI)
  - CLI command siap pakai: invctrl

---

## SCREESHOOT
