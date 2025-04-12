---
layout: default
title: Instalasi
---

# Instalasi & Menjalankan InvCtrl

## 1. Install Python

Unduh dan install Python dari [https://www.python.org/downloads/](https://www.python.org/downloads/)

Pastikan saat install:
- Checklist **"Add Python to PATH"**
- Setelah selesai, cek versi:
  ```python --version```

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
  
## 2. Install InvCtrl dari PyPI
  ```
  pip install invctrl
  ```
    

## 3. Jalankan Aplikasi
  ```
  invctrl
  ```

## 4. Install via Github

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
