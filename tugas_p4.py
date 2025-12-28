isi={"nama": "tv", "kategori": "elektronik", "jumlah": 5, "harga": 5000000}
input_kategori = input("Masukkan kategori barang (elektronik/bukan): ")
for isi in [isi]:
    if isi["kategori"] == input_kategori:
        total = isi["jumlah"] * isi["harga"] - 100000
    else:
        total = isi["jumlah"] * isi["harga"]
    print("Total:", total)