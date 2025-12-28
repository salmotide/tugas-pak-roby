ujian = int(input("Masukkan nilai ujian: "))
if ujian >= 80:
    print("Lulus dengan syarat masuk ke tahap berikutnya")
    kesehatan = int(input("Berapa Angka Kesehatan anda?: "))
    kehadiran = int(input("Masukkan persentase kehadiran Anda: "))
    if kesehatan >= 75 and kehadiran >= 70:
        print("Anda LULUS")
    else:
        print("tidak bisa lulus karena nilai kehadiran atau kesehatan kurang")
else:
    print("tidak bisa lanjut karena nilai ujian kurang")

