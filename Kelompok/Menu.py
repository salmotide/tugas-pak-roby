import Salomo_Perpustakaan
import Andhika_Pembelian
import Raffy_Pemijaman
import salomo_Pengembalian

while True:
    print("\n=== MENU UTAMA PERPUSTAKAAN ===")
    print("1. Kelola Perpustakaan")
    print("2. Pembelian Buku")
    print("3. Peminjaman Buku")
    print("4. Pengembalian Buku")
    print("5. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        Salomo_Perpustakaan.menu_perpus()
    elif pilih == "2":
        Andhika_Pembelian.menu_andhika()
    elif pilih == "3":
        Raffy_Pemijaman.menu_raffy()
    elif pilih == "4":
        salomo_Pengembalian.menu_pengembalian()
    elif pilih == "5":
        print("Terima kasih 🙏")
        break
