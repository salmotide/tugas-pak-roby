import json
import os
from datetime import datetime
import Salomo_Perpustakaan as Perpus

FILE = "data_peminjaman.json"
data_peminjaman = []


def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            if f.read().strip():
                f.seek(0)
                data_peminjaman.clear()
                data_peminjaman.extend(json.load(f))


def save():
    with open(FILE, "w") as f:
        json.dump(data_peminjaman, f, indent=4)


def menu():
    print("\n=== PEMINJAMAN BUKU ===")
    print("1. Tambah Peminjaman")
    print("2. Lihat Data Peminjaman")
    print("3. Kembali")
    return input("Pilih: ")


def tambah_data():
    Perpus.tampilkan_buku()

    nama = input("Nama Peminjam: ").strip()
    judul = input("Judul Buku: ").strip()

    buku = Perpus.cari_buku(judul)
    if not buku or buku["stok"] <= 0:
        print("Buku tidak tersedia")
        return

    buku["stok"] -= 1
    Perpus.save_buku()

    data_peminjaman.append({
        "nama": nama,
        "judul": judul,
        "tanggal_pinjam": datetime.now().strftime("%d/%m/%Y")
    })

    save()
    print("Peminjaman berhasil")


def tampilkan_data():
    print("\n=== DATA PEMINJAMAN ===")
    if not data_peminjaman:
        print("Belum ada data")
    else:
        for i, d in enumerate(data_peminjaman, 1):
            print(f"{i}. {d['nama']} | {d['judul']} | {d['tanggal_pinjam']}")


def menu_raffy():
    load()
    while True:
        p = menu()
        if p == "1":
            tambah_data()
        elif p == "2":
            tampilkan_data()
            input("Enter untuk lanjut...")
        elif p == "3":
            break
