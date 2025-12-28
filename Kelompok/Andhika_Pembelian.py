import json
import os
import Salomo_Perpustakaan as Perpus

FILE = "data_pembelian.json"
data_pembelian = []


def load():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                if f.read().strip():
                    f.seek(0)
                    data_pembelian.extend(json.load(f))
        except json.JSONDecodeError:
            pass


def save():
    with open(FILE, "w") as f:
        json.dump(data_pembelian, f, indent=4)


load()



def menu_andhika():
    Perpus.tampilkan_buku()

    while True:
        print("\n=== PEMBELIAN BUKU ===")
        print("1. Tambah Pembelian")
        print("2. Lihat Data")
        print("3. Kembali")

        p = input("Pilih: ")

        if p == "1":
            tambah_data()
        elif p == "2":
            tampilkan_data()
        elif p == "3":
            break
        else:
            print("Pilihan salah")



def tambah_data():
    judul = input("Judul Buku: ").strip()
    buku = Perpus.cari_buku(judul)

    if not buku:
        print("Buku tidak ada di perpustakaan")
        return

    if buku["stok"] <= 0:
        print("Stok habis")
        return

    while True:
        jml = input("Jumlah beli: ")
        if jml.isdigit():
            jumlah = int(jml)
            break
        print("Jumlah harus angka")

    if jumlah > buku["stok"]:
        print("Stok tidak cukup")
        return

    total = jumlah * buku["harga"]

    buku["stok"] -= jumlah
    Perpus.save_buku()

    data_pembelian.append({
        "judul": judul,
        "jumlah": jumlah,
        "harga": buku["harga"],
        "total": total
    })

    save()
    print("Pembelian berhasil")


def tampilkan_data():
    print("\n=== DATA PEMBELIAN ===")
    if not data_pembelian:
        print("Belum ada data")
    else:
        for i, d in enumerate(data_pembelian, 1):
            print(
                f"{i}. {d.get('judul','-')} | "
                f"{d.get('jumlah',0)} x Rp{d.get('harga',0)} "
                f"= Rp{d.get('total',0)}"
            )
    input("\nEnter untuk kembali...")
