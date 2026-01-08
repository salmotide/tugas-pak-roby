import Salomo_Perpustakaan
import Andhika_Pembelian
import Raffy_Pemijaman

while True:
    print("\n=== MENU UTAMA PERPUSTAKAAN ===")
    print("1. Kelola Perpustakaan")
    print("2. Pembelian Buku")
    print("3. Peminjaman Buku")
    print("4. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        Salomo_Perpustakaan.menu_perpus_097()
    elif pilih == "2":
        Andhika_Pembelian.menu_078()
    elif pilih == "3":
        Raffy_Pemijaman.menu_raffy_064()
    elif pilih == "4":
        print("Terima kasih 🙏")
        break
