def pelanggan():#0064
    print("---Input Data Peminjam buku---")
    nama = input("Masukan Nama Peminjam buku: ")
    buku = input("Masukan Judul buku yang dipinjam: ")

    pelanggan_baru ={
        "nama" : nama,
        "buku" : buku
    }

    data_pelanggan.append(pelanggan_baru)
    print(f"Data {nama} berhasil di masukan ke sistem")

data_pelanggan = []

def lihatpelanggan():
    print("---List Peminjam---")
    if not data_pelanggan:
        print("List Kosong")
    else:
        for a, b in enumerate(data_pelanggan, 1):
            print(f"{a}. Nama Peminjam: {b['nama']} | Judul buku: {b['buku']}")

def edit_pelanggan():
    lihatpelanggan()
    if not data_pelanggan:
        return
    print ("---Edit data---")
    try:
        urutan = int(input("Masukan nomor urut yang ingin diedit: "))
        index = urutan - 1

        if 0 <= index < len(data_pelanggan):
            data_saat_ini = data_pelanggan[index]

            print(f"Data Lama -> Nama: {data_saat_ini['nama']} | Buku: {data_saat_ini['buku']}")
            print("(Biarkan kosong dan tekan Enter jika tidak ingin mengubah data)")

            nama_baru = input("Masukan Nama Baru: ")
            buku_baru = input("Masukan Judul buku baru: ")

            if  len(nama_baru.strip()) > 0:
                data_pelanggan[index]['nama'] = nama_baru

            if len(buku_baru.strip()) > 0:
                data_pelanggan[index]['buku'] = buku_baru

            print("Data berhasil diperbarui")
        else:
            print("Nomor tidak ditemukan")
    except ValueError:
        print("Error: Harap masukan angka")

def hapus_pelanggan():
    lihatpelanggan()
    if not data_pelanggan:
        return
    print("---Hapus Data---")
    try:
        urutan = int(input("Masukan nomor urut yang ingin dihapus: "))
        if 0 < urutan <= len(data_pelanggan):
            data_terhapus = data_pelanggan.pop(urutan - 1)
            print(f"Data '{data_terhapus['nama']}' berhasil dihapus")
        else:
            print("Nomor tidak ditemukan")

    except ValueError:
        print("Error: Harap masukan angka, bukan huruf")

while True:
    print("~~Perpustakaan~~")
    print("1. Tambah Data Peminjam Buku")
    print("2. Lihat Data Peminjam Buku")
    print("3. Edit Data Peminjam Buku")
    print("4. Hapus Data Peminjam Buku") 
    print("5. Keluar")

    try:
        pilih = int(input("Pilih Menu : "))

        if pilih == 1:
            pelanggan()
        elif pilih == 2:
            lihatpelanggan()
        elif pilih == 3:
            edit_pelanggan()
        elif pilih == 4:
            hapus_pelanggan()
        elif pilih == 5:
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukan harus berupa angka.")