def program_kasir_buku():
    daftar_buku_toko = [
        {"kode": "B001", "judul": "Laskar Pelangi", "harga": 75000},
        {"kode": "B002", "judul": "Bumi - Tere Liye", "harga": 89000},
        {"kode": "B003", "judul": "Negeri 5 Menara", "harga": 68000},
        {"kode": "B004", "judul": "Atomic Habits", "harga": 120000},
        {"kode": "B005", "judul": "The Psychology of Money", "harga": 135000},
        {"kode": "B006", "judul": "Dilan 1990", "harga": 60000},
        {"kode": "B007", "judul": "Pulang - Tere Liye", "harga": 95000},
        {"kode": "B008", "judul": "Rich Dad Poor Dad", "harga": 99000},
        {"kode": "B009", "judul": "Filosofi Teras", "harga": 72000},
        {"kode": "B010", "judul": "Sherlock Holmes", "harga": 85000},
    ]

    print("=========================================")
    print("   SISTEM KASIR: TOKO BUKU + VALIDASI")
    print("=========================================")

    # Tampilkan daftar buku
    print("\n📚 DAFTAR BUKU TERSEDIA:")
    print("-----------------------------------------")
    for buku in daftar_buku_toko:
        print(f"{buku['kode']} | {buku['judul']} | Rp {buku['harga']:,.2f}")
    print("-----------------------------------------")

    daftar_beli = []


    print("\n--- Masukkan KODE atau NAMA buku (ketik 'stop' utk selesai) ---")

    while True:
        pilihan = input("Masukkan kode/nama buku: ")

        if pilihan.lower() == "stop":
            break

        buku_ditemukan = None
        for b in daftar_buku_toko:
            if pilihan.upper() == b["kode"] or pilihan.lower() == b["judul"].lower():
                buku_ditemukan = b
                break

        if buku_ditemukan:
            daftar_beli.append(buku_ditemukan)
            print(f"✔ '{buku_ditemukan['judul']}' ditambahkan ke keranjang.\n")
        else:
            print("❌ Buku tidak ditemukan! Tidak bisa ditambahkan.\n")

    if len(daftar_beli) == 0:
        print("\n❌ Tidak ada buku dibeli. Transaksi dibatalkan.")
        return
    
    print("\n=== 🛒 DAFTAR BUKU YANG DIBELI ===")
    total = 0

    for i, b in enumerate(daftar_beli, start=1):
        print(f"{i}. {b['judul']} - Rp {b['harga']:,.2f}")
        total += b["harga"]

    print(f"\nTOTAL BAYAR: Rp {total:,.2f}")


    print("\n--- METODE PEMBAYARAN ---")
    metode = input("Pilih metode pembayaran (DEBIT/LAIN): ").upper()

    if metode == "DEBIT":
        print("Memproses pembayaran DEBIT...")
    elif metode == "LAIN":
        metode2 = input("TUNAI/KREDIT/QRIS: ").upper()
        if metode2 not in ["TUNAI", "KREDIT", "QRIS"]:
            print("❌ Metode tidak valid. Transaksi dibatalkan.")
            return
        print(f"Memproses pembayaran {metode2}...")
    else:
        print("❌ Metode tidak valid. Transaksi dibatalkan.")
        return

    print("\n=========================================")
    print("🎉 PEMBAYARAN BERHASIL! TERIMA KASIH.")
    print("=========================================")



program_kasir_buku()
