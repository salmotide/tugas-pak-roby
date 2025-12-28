def program_kasir_buku():
    """
    Simulasi proses kasir buku tanpa opsi kado, dengan perulangan input
    dan percabangan metode pembayaran (Debit vs Lain).
    """
    print("=========================================")
    print("  SISTEM KASIR: TOKO BUKU DEMO")
    print("=========================================")
    
    total_harga = 0.0
    
    # --- PERULANGAN (Looping): Input Harga Buku ---
    print("\n--- 🛒 INPUT BUKU (Ketik 0 jika sudah selesai) ---")
    
    while True:
        try:
            # Meminta input harga buku
            harga_buku = float(input("Masukkan harga buku ke kasir (0 untuk selesai): Rp "))
            
            if harga_buku > 0:
                # Akumulasi total harga
                total_harga += harga_buku
                print(f"Buku ditambahkan. Total sementara: Rp {total_harga:,.2f}")
            elif harga_buku == 0:
                # Kondisi keluar dari perulangan
                break 
            else:
                print("Harga tidak valid. Harap masukkan nilai positif.")
        except ValueError:
            print("Input salah. Harap masukkan angka.")
            
    if total_harga == 0:
        print("\n--- ❌ Tidak ada buku yang dibeli. Transaksi dibatalkan. ---")
        return

    print(f"\n--- TOTAL AKHIR: Rp {total_harga:,.2f} ---")

    # --- PERCABANGAN: Metode Pembayaran (Debit vs Lain) ---
    print("\n--- 💳 PROSES PEMBAYARAN ---")
    metode_bayar = input("Pilih metode pembayaran (DEBIT / LAIN): ").upper()
    
    # Percabangan IF-ELSE IF (elif)
    if metode_bayar == "DEBIT":
        print("✅ Memproses pembayaran DEBIT...")
        print("Instruksi: Pelanggan harap gesek/masukkan kartu.")
    elif metode_bayar == "LAIN":
        metode_spesifik = input("Metode Lain apa? (TUNAI/KREDIT/QRIS): ").upper()
        
        if metode_spesifik in ["TUNAI", "KREDIT", "QRIS"]:
            print(f"✅ Memproses pembayaran dengan {metode_spesifik}.")
            if metode_spesifik == "QRIS":
                print("Kasir menampilkan kode QR untuk di-scan.")
        else:
            print("\n⚠️ Pilihan Metode Lain tidak spesifik. Transaksi DIBATALKAN.")
            return
    else:
        # Penanganan kasus jika input tidak sesuai
        print("\n⚠️ Metode pembayaran tidak valid. Transaksi DIBATALKAN.")
        return

    print("\n=========================================")
    print("PEMBAYARAN SUKSES! Buku diserahkan.")
    print("👋 TERIMA KASIH TELAH BERBELANJA.")
    print("=========================================")

# Jalankan Program untuk Demostrasi
program_kasir_buku()