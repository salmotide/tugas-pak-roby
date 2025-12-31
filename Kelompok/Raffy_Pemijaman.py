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
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Kembali")
    return input("Pilih: ")


def tambah_data():
    Perpus.tampilkan_buku()

    nama = input("Nama Peminjam: ").strip()
    judul = input("Judul Buku: ").strip()

    buku = Perpus.cari_buku(judul)
    if not buku or buku["stok"] <= 0:
        print("❌ Buku tidak tersedia")
        return

    buku["stok"] -= 1
    Perpus.save_buku()

    data_peminjaman.append({
        "nama": nama,
        "judul": judul,
        "tanggal_pinjam": datetime.now().strftime("%d/%m/%Y")
    })

    save()
    print("✅ Peminjaman berhasil")


def tampilkan_data():
    print("\n=== DATA PEMINJAMAN ===")
    if not data_peminjaman:
        print("Belum ada data")
    else:
        for i, d in enumerate(data_peminjaman, 1):
            print(f"{i}. Nama   : {d['nama']}")
            print(f"   Buku   : {d['judul']}")
            print(f"   Tanggal: {d['tanggal_pinjam']}")
            print("---------------------------------")


def update_data():
    tampilkan_data()
    if not data_peminjaman:
        return

    try:
        idx = int(input("Pilih nomor data yang diupdate: ")) - 1
        if idx < 0 or idx >= len(data_peminjaman):
            print("❌ Nomor tidak valid")
            return

        data_peminjaman[idx]["nama"] = input("Nama baru: ")
        data_peminjaman[idx]["judul"] = input("Judul buku baru: ")
        data_peminjaman[idx]["tanggal_pinjam"] = datetime.now().strftime("%d/%m/%Y")

        save()
        print("✅ Data peminjaman berhasil diupdate")

    except ValueError:
        print("❌ Input harus angka")


def hapus_data():
    tampilkan_data()
    if not data_peminjaman:
        return

    try:
        idx = int(input("Pilih nomor data yang dihapus: ")) - 1
        if idx < 0 or idx >= len(data_peminjaman):
            print("❌ Nomor tidak valid")
            return

        judul = data_peminjaman[idx]["judul"]

        buku = Perpus.cari_buku(judul)
        if buku:
            buku["stok"] += 1
            Perpus.save_buku()

        del data_peminjaman[idx]
        save()
        print("✅ Data peminjaman berhasil dihapus")

    except ValueError:
        print("❌ Input harus angka")


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
            update_data()
        elif p == "4":
            hapus_data()
        elif p == "5":
            break
        else:
            print("❌ Pilihan tidak valid")
