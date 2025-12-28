nmsiswa = input("Masukkan nama siswa: ")
while True:
    try:
        jumpel = int(input("Masukkan jumlah pelajaran yang diambil: "))
        if jumpel > 0:
            break
        else:
            print("Jumlah pelajaran harus lebih dari 0. Silakan coba lagi.")
    except ValueError:
        print("Input salah. Harap masukkan angka bulat positif.")
        
tonil = 0.0
    
for i in range(1, jumpel + 1):
    while True:
        try:
            nilai = float(input(f"Masukkan nilai pelajaran ke-{i}: "))
            if 0 <= nilai <= 100:
                tonil += nilai
                break
            else:
                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")   
        except ValueError:
            print("Input salah. Harap masukkan angka antara 0 dan 100.")

rata2 = tonil / jumpel

if rata2 >= 70:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("\n=========================================")
print(f"Siswa: {nmsiswa}")
print(f"Jumlah Pelajaran: {jumpel}")
print(f"Total Nilai: {tonil:.2f}")
print(f"Rata-rata: {rata2:.2f}")
print(f"Status: {status}")
print("=========================================")