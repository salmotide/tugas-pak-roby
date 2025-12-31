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
                    data_pembelian.clear()
                    data_pembelian.extend(json.load(f))
        except json.JSONDecodeError:
            pass


def save():
    with open(FILE, "w") as f:
        json.dump(data_pembelian, f, indent=4)


load()

def menu():
    print("\n=== PEMBELIAN BUKU ===")
    print("1. Tambah Pembelian")
    print("2. Lihat Data Pembelian")
    print("3. Update Pembelian")
    print("4. Hapus Pembelian")
    print("5. Kembali")
    return input("Pilih: ")

def tambah_data():
    Perpus.tampilkan_buku()

    judul = input("Judul Buku: ").strip()
    buku = Perpus.cari_buku(judul)

    if not buku:
        print("❌ Buku tidak ada di perpustakaan")
        return

    if buku["stok"] <= 0:
        print("❌ Stok habis")
        return

    while True:
        jml = input("Jumlah beli: ")
        if jml.isdigit():
            jumlah = int(jml)
            break
        print("❌ Jumlah harus angka")

    if jumlah > buku["stok"]:
        print("❌ Stok tidak cukup")
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
    print("✅ Pembelian berhasil")

def tampilkan_data():
    print("\n=== DATA PEMBELIAN ===")
    if not data_pembelian:
        print("Belum ada data")
    else:
        for i, d in enumerate(data_pembelian, 1):
            print("----------------------------------")
            print(f"No     : {i}")
            print(f"Judul  : {d['judul']}")
            print(f"Jumlah : {d['jumlah']}")
            print(f"Harga  : Rp {d['harga']:,}")
            print(f"Total  : Rp {d['total']:,}")
    print("----------------------------------")

def update_data():
    tampilkan_data()
    if not data_pembelian:
        return

    try:
        idx = int(input("Pilih nomor data yang diupdate: ")) - 1
        if idx < 0 or idx >= len(data_pembelian):
            print("❌ Nomor tidak valid")
            return

        data = data_pembelian[idx]

        buku_lama = Perpus.cari_buku(data["judul"])
        if buku_lama:
            buku_lama["stok"] += data["jumlah"]

        judul_baru = input("Judul Buku Baru: ").strip()
        buku_baru = Perpus.cari_buku(judul_baru)

        if not buku_baru or buku_baru["stok"] <= 0:
            print("❌ Buku tidak tersedia")
            return

        jumlah_baru = int(input("Jumlah Baru: "))
        if jumlah_baru > buku_baru["stok"]:
            print("❌ Stok tidak cukup")
            return

        buku_baru["stok"] -= jumlah_baru
        Perpus.save_buku()

        data["judul"] = judul_baru
        data["jumlah"] = jumlah_baru
        data["harga"] = buku_baru["harga"]
        data["total"] = jumlah_baru * buku_baru["harga"]

        save()
        print("✅ Data pembelian berhasil diupdate")

    except ValueError:
        print("❌ Input harus angka")


def hapus_data():
    tampilkan_data()
    if not data_pembelian:
        return

    try:
        idx = int(input("Pilih nomor data yang dihapus: ")) - 1
        if idx < 0 or idx >= len(data_pembelian):
            print("❌ Nomor tidak valid")
            return

        data = data_pembelian[idx]

        # kembalikan stok
        buku = Perpus.cari_buku(data["judul"])
        if buku:
            buku["stok"] += data["jumlah"]
            Perpus.save_buku()

        del data_pembelian[idx]
        save()
        print("✅ Data pembelian berhasil dihapus")

    except ValueError:
        print("❌ Input harus angka")


def menu_andhika():
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
            print("❌ Pilihan salah")
