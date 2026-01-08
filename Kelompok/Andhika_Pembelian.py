data_transaksi = []

def menu_078():
    print("\n=== Data Transaksi Pembelian Buku ===")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Data Transaksi")
    print("3. Perbarui Data Transaksi")
    print("4. Hapus Data Transaksi")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    return pilihan

def tambah_data_078():
    print("\n--- TAMBAH TRANSAKSI BARU ---")
    id_transaksi = input("Masukkan ID Transaksi: ")
    nama = input("Masukkan Nama Pelanggan: ")
    judul = input("Masukkan Judul Buku: ")
    
    while True:
        harga_input = input("Masukkan Harga Buku (Rp): ")
        harga_input = harga_input.replace(".", "")  
        harga_input = harga_input.replace(",", "") 
        try:
            harga = int(harga_input)
            break
        except:
            print("Harga harus berupa angka!")
    
    print(f"Total: Rp {harga:,}".replace(",", "."))
    
    print("\nMetode Pembayaran:")
    print("1. Debit")
    print("2. Tunai") 
    print("3. Kartu Kredit")
    print("4. QRIS")
    pilih = input("Pilih (1-4): ")
    
    if pilih == "1":
        metode = "Debit"
    elif pilih == "2":
        metode = "Tunai"
    elif pilih == "3":
        metode = "Kartu Kredit"
    elif pilih == "4":
        metode = "QRIS"
    else:
        metode = "Tunai"
    
    if metode == "Debit":
        print("Silakan gesek kartu...")
    else:
        print(f"Proses pembayaran {metode}...")
    
    transaksi_baru = {
        "ID": id_transaksi,
        "Nama": nama,
        "Judul": judul,
        "Harga": harga,
        "Metode": metode,
        "Status": "Selesai"
    }
    data_transaksi.append(transaksi_baru)
    
    print("\nTransaksi berhasil!")
    print("Pelanggan menerima buku.")

def tampilkan_data_078():
    if len(data_transaksi) == 0:
        print("\nBelum ada data")
    else:
        print("\n--- DAFTAR TRANSAKSI ---")
        for i in range(len(data_transaksi)):
            t = data_transaksi[i]
            print(f"\n[{i}] ID: {t['ID']}")
            print(f"Nama: {t['Nama']}")
            print(f"Buku: {t['Judul']}")
            print(f"Harga: Rp {t['Harga']:,}".replace(",", "."))
            print(f"Metode: {t['Metode']}")
            print(f"Status: {t['Status']}")

def perbarui_data_078():
    print("\n--- UPDATE DATA ---")
    id_cari = input("ID Transaksi yang mau diupdate: ")
    
    ketemu = False
    for t in data_transaksi:
        if t["ID"] == id_cari:
            ketemu = True
            print(f"\nData sekarang:")
            print(f"Nama: {t['Nama']}")
            print(f"Judul: {t['Judul']}")
            
            nama_baru = input("Nama baru: ")
            judul_baru = input("Judul baru: ")
            
            t["Nama"] = nama_baru
            t["Judul"] = judul_baru
            
            print("\nData berhasil diupdate!")
            break
    
    if not ketemu:
        print("ID tidak ditemukan")

def hapus_data_078():
    print("\n--- HAPUS DATA ---")
    id_cari = input("ID Transaksi yang mau dihapus: ")
    
    ketemu = False
    for t in data_transaksi:
        if t["ID"] == id_cari:
            ketemu = True
            data_transaksi.remove(t)
            print("\nData berhasil dihapus!")
            break
    
    if not ketemu:
        print("ID tidak ditemukan")

while True:
    pilihan = menu_078()
    if pilihan == "1":
        tambah_data_078()
    elif pilihan == "2":
        tampilkan_data_078()
    elif pilihan == "3":
        perbarui_data_078()
    elif pilihan == "4":
        hapus_data_078()
    elif pilihan == "5":
        print("\nTerima kasih!")
        break
    else:
        print("Pilihan salah!")
    
    input("\nEnter untuk lanjut...")