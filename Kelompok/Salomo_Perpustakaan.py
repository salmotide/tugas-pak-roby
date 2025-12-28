import json
import os

FILE = "data_buku.json"
data_buku = []


def load_buku():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                if f.read().strip():
                    f.seek(0)
                    data_buku.clear()
                    data_buku.extend(json.load(f))
        except json.JSONDecodeError:
            pass


def save_buku():
    with open(FILE, "w") as f:
        json.dump(data_buku, f, indent=4)


load_buku()


def cari_buku(judul):
    for b in data_buku:
        if b["judul"].lower() == judul.lower():
            return b
    return None


def tampilkan_buku():
    print("\n=== DAFTAR BUKU PERPUSTAKAAN ===")
    if not data_buku:
        print("Belum ada buku")
    else:
        for i, b in enumerate(data_buku, 1):
            print(
                f"{i}. {b.get('judul','-')} | "
                f"Stok: {b.get('stok',0)} | "
                f"Harga: Rp{b.get('harga',0)}"
            )
    input("\nEnter untuk lanjut...")


def tambah_buku():
    judul = input("Judul Buku: ").strip()
    if cari_buku(judul):
        print("Buku sudah ada")
        return

    while True:
        s = input("Stok: ")
        if s.isdigit():
            stok = int(s)
            break
        print("Stok harus angka")

    while True:
        h = input("Harga: ")
        if h.isdigit():
            harga = int(h)
            break
        print("Harga harus angka")

    data_buku.append({
        "judul": judul,
        "stok": stok,
        "harga": harga
    })

    save_buku()
    print("Buku berhasil ditambahkan")


def edit_buku():
    tampilkan_buku()
    judul = input("Judul buku yang mau diedit: ")

    buku = cari_buku(judul)
    if not buku:
        print("Buku tidak ditemukan")
        return

    print("(Kosongkan jika tidak diubah)")
    judul_baru = input("Judul baru: ")
    stok_baru = input("Stok baru: ")
    harga_baru = input("Harga baru: ")

    if judul_baru.strip():
        buku["judul"] = judul_baru

    if stok_baru.isdigit():
        buku["stok"] = int(stok_baru)

    if harga_baru.isdigit():
        buku["harga"] = int(harga_baru)

    save_buku()
    print("Data buku berhasil diperbarui")



def hapus_buku():
    tampilkan_buku()
    judul = input("Judul buku yang mau dihapus: ")

    buku = cari_buku(judul)
    if not buku:
        print("Buku tidak ditemukan")
        return

    data_buku.remove(buku)
    save_buku()
    print("Buku berhasil dihapus")



def menu_perpus():
    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Lihat Buku")
        print("2. Tambah Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Kembali")

        p = input("Pilih: ")

        if p == "1":
            tampilkan_buku()
        elif p == "2":
            tambah_buku()
        elif p == "3":
            edit_buku()
        elif p == "4":
            hapus_buku()
        elif p == "5":
            break
        else:
            print("Pilihan salah")
