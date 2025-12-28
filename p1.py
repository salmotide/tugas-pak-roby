nama = input("Masukkan nama Anda: ")
norut = input("Masukkan nomor urut mahasiswa: ")

if norut.isnumeric():norut = int (norut)
else:
    print("Harus angka")
    exit(1)

if(norut > 30 or norut < 1):
    print("Nomor urut tidak valid")
else:
    print(f"Nama: {nama}")
    print(f"Nomor Urut: {norut}")
    
    if(norut >= 1 and norut <= 10):
        print("Kelompok 1")
    elif(norut >= 11 and norut <= 20):
        print("Kelompok 2")
    elif(norut >= 21 and norut <= 30):
        print("Kelompok 3")