import json
import os
from datetime import datetime
import Salomo_Perpustakaan as Perpus

FILE_PINJAM = "data_peminjaman.json"
FILE_KEMBALI = "data_pengembalian.json"

data_pengembalian = []

def load_pengembalian():
    if os.path.exists(FILE_KEMBALI):
        with open(FILE_KEMBALI, "r") as f:
            if f.read().strip():
                f.seek(0)
                data_pengembalian.clear()
                data_pengembalian.extend(json.load(f))


def save_pengembalian():
    with open(FILE_KEMBALI, "w") as f:
        json.dump(data_pengembalian, f, indent=4)


def load_peminjaman():
    if not os.path.exists(FILE_PINJAM):
        return []

    with open(FILE_PINJAM, "r") as f:
        if not f.read().strip():
            return []
        f.seek(0)
        return json.load(f)

def menu_pengembalian():
    load_pengembalian()
    while True:
        print("\n=== MENU PENGEMBALIAN ===")
        print("1. Kembalikan Buku")
        print("2. Lihat Data Pengembalian")
        print("3. Update Data Pengembalian")
        print("4. Hapus Data Pengembalian")
        print("5. Kembali")

        p = input("Pilih: ")

        if p == "1":
            kembalikan_buku()
        elif p == "2":
            tampilkan_pengembalian()
            input("Enter untuk lanjut...")
        elif p == "3":
            update_pengembalian()
        elif p == "4":
            hapus_pengembalian()
        elif p == "5":
            break
        else:
            print("❌ Pilihan salah")

def kembalikan_buku():
    data_peminjaman = load_peminjaman()

    if not data_peminjaman:
        print("Belum ada data peminjaman")
        return

    print("\n=== DAFTAR PEMINJAMAN ===")
    for i, d in enumerate(data_peminjaman, 1):
        print(f"{i}. {d['nama']} | {d['judul']} | {d['tanggal_pinjam']}")

    try:
        pilih = int(input("Pilih nomor yang dikembalikan: ")) - 1
        data = data_peminjaman.pop(pilih)
    except:
        print("❌ Pilihan tidak valid")
        return

    tanggal_kembali = datetime.now()
    tanggal_pinjam = datetime.strptime(data["tanggal_pinjam"], "%d/%m/%Y")
    durasi = (tanggal_kembali - tanggal_pinjam).days

    buku = Perpus.cari_buku(data["judul"])
    if buku:
        buku["stok"] += 1
        Perpus.save_buku()

    data_pengembalian.append({
        "nama": data["nama"],
        "judul": data["judul"],
        "tanggal_pinjam": data["tanggal_pinjam"],
        "tanggal_kembali": tanggal_kembali.strftime("%d/%m/%Y"),
        "durasi_hari": durasi
    })

    with open(FILE_PINJAM, "w") as f:
        json.dump(data_peminjaman, f, indent=4)

    save_pengembalian()
    print("✅ Buku berhasil dikembalikan")


def tampilkan_pengembalian():
    print("\n=== DATA PENGEMBALIAN ===")
    if not data_pengembalian:
        print("Belum ada data")
        return

    for i, d in enumerate(data_pengembalian, 1):
        print("----------------------------------")
        print(f"No              : {i}")
        print(f"Nama            : {d.get('nama','-')}")
        print(f"Judul Buku      : {d.get('judul','-')}")
        print(f"Tgl Pinjam      : {d.get('tanggal_pinjam','-')}")
        print(f"Tgl Kembali     : {d.get('tanggal_kembali','-')}")
        print(f"Durasi (hari)   : {d.get('durasi_hari','-')}")
    print("----------------------------------")

def update_pengembalian():
    tampilkan_pengembalian()
    if not data_pengembalian:
        return

    try:
        idx = int(input("Pilih nomor data yang diupdate: ")) - 1
        if idx < 0 or idx >= len(data_pengembalian):
            print("❌ Nomor tidak valid")
            return

        data = data_pengembalian[idx]

        data["nama"] = input("Nama Baru        : ")
        data["judul"] = input("Judul Buku Baru  : ")

        t_pinjam = datetime.strptime(data["tanggal_pinjam"], "%d/%m/%Y")
        t_kembali = datetime.strptime(data["tanggal_kembali"], "%d/%m/%Y")
        data["durasi_hari"] = (t_kembali - t_pinjam).days

        save_pengembalian()
        print("✅ Data pengembalian berhasil diupdate")

    except ValueError:
        print("❌ Input harus angka")

def hapus_pengembalian():
    tampilkan_pengembalian()
    if not data_pengembalian:
        return

    try:
        idx = int(input("Pilih nomor data yang dihapus: ")) - 1
        if idx < 0 or idx >= len(data_pengembalian):
            print("❌ Nomor tidak valid")
            return

        del data_pengembalian[idx]
        save_pengembalian()
        print("✅ Data pengembalian berhasil dihapus")

    except ValueError:
        print("❌ Input harus angka")
