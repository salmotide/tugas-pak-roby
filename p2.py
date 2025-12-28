# operasi aritmatika
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

c = a + b
print("hasil %d + %d = %d" % (a, b, c))

c = a - b
print("hasil %d - %d = %d" % (a, b, c))

c = a * b
print("hasil %d * %d = %d" % (a, b, c))

c = a / b
print("hasil %d / %d = %.1f" % (a, b, c))

a = int(input("Masukkan nilai a: "))

# operasi penugasan
a += 5
a -= 5
a *= 5
a /= 5
print("nilai setelah di tambah 5", a)
print("a = %d" % a)

# operasi relasional
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

c = a == b
print("hasil %d == %d = %s" % (a, b, c))

c = a < b
print("hasil %d < %d = %s" % (a, b, c))

c = a > b
print("hasil %d > %d = %s" % (a, b, c))

c = a != b
print("hasil %d != %d = %s" % (a, b, c))

# operasi logika
a = True
b = False

c = a and b
print("hasil %r and %r = %r" % (a, b, c))

c = a or b
print("hasil %r or %r = %r" % (a, b, c))

c = not a
print("hasil not %r = %r" % (a, c))

# percabangan
umur = int(input("Masukkan umur Anda: "))
aku = "bocah" if umur < 10 else "dewasa"
print(aku)

# Soal 1
# Cek suhu tubuh
suhu = int(input("Masukkan angka suhu: "))
if suhu < 34:
    if suhu >= 31 and suhu <= 32:
        print("Demam ringan")
    elif suhu <= 33:
        print("Demam sedang")
    else:
        print("Tidak demam")
else:
    print("Demam tinggi")

