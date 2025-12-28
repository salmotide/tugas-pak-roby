# angka = int(input("Masukkan angka: "))
# if angka == 1:
#     print("Satu")
# elif angka == 2:
#     print("Dua")
# elif angka == 3:
#     print("Tiga")
# else:
#     text = "angka tidak valid"
# print("nilai: %s" % text)

usename = input("Masukkan username: ")
password = input("Masukkan password: ")
if usename == "admin" and password == "admin123":
    level = input("Masukkan level: ")
    if(level == "superadmin"):
        print("Selamat datang Superadmin")
    elif(level == "admin"):
        print("Selamat datang Admin")
    elif(level == "user"):
        print("Selamat datang User")
    else:
        print("Anda tidak berhak mengakses sistem ini")
else:
    print("Username atau password salah")