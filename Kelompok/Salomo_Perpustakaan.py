def menu_perpus_097():
    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Lihat Buku")
        print("2. Tambah Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Kembali")

        p = input("Pilih: ")

        if p == "1":
            tampilkan_buku_097()
        elif p == "2":
            tambah_buku_097()
        elif p == "3":
            edit_buku_097()
        elif p == "4":
            hapus_buku_097()
        elif p == "5":
            break
        else:
            print("Pilihan salah")

def edit_buku_097():
    tampilkan_buku_097()
    judul = input("Judul buku yang diedit: ")

    buku = cari_buku_097(judul)
    if not buku:
        print("Buku tidak ditemukan")
        return

    print("(Kosongkan jika tidak diubah)")
    buku["judul"] = input("Judul Baru   : ") or buku["judul"]
    buku["penulis"] = input("Penulis Baru : ") or buku["penulis"]
    buku["tahun"] = input("Tahun Baru   : ") or buku["tahun"]

    stok = input("Stok Baru    : ")
    harga = input("Harga Baru   : ")

    if stok.isdigit():
        buku["stok"] = int(stok)
    if harga.isdigit():
        buku["harga"] = int(harga)

    print("Data buku berhasil diperbarui")

def tambah_buku_097():
    judul = input("Judul Buku     : ")
    if cari_buku_097(judul):
        print("Buku sudah ada")
        return

    penulis = input("Penulis        : ")
    penerbit = input("Penerbit       : ")
    tahun = input("Tahun Terbit   : ")

    while True:
        stok = input("Stok           : ")
        if stok.isdigit():
            stok = int(stok)
            break
        print("Stok harus angka!")

    while True:
        harga = input("Harga          : ")
        if harga.isdigit():
            harga = int(harga)
            break
        print("Harga harus angka!")

    data_buku.append({
        "judul": judul,
        "penulis": penulis,
        "penerbit": penerbit,
        "tahun": tahun,
        "stok": stok,
        "harga": harga
    })

    print("Buku berhasil ditambahkan")


def cari_buku_097(judul):
    for buku in data_buku:
        if buku["judul"].lower() == judul.lower():
            return buku
    return None
data_buku = []

def hapus_buku_097():
    judul = input("Judul buku yang dihapus: ")

    buku = cari_buku_097(judul)
    if not buku:
        print("Buku tidak ditemukan")
        return

    data_buku.remove(buku)
    print("Buku berhasil dihapus")

def tampilkan_buku_097():
    print("\n=== DAFTAR BUKU ===")
    if not data_buku:
        print("Belum ada data buku")
    else:
        for i, b in enumerate(data_buku, 1):
            print(f"""{i}.
Judul     : {b['judul']}
Penulis   : {b['penulis']}
Penerbit  : {b['penerbit']}
Tahun     : {b['tahun']}
Stok      : {b['stok']}
Harga     : Rp{b['harga']}
""")
