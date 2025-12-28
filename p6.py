mhs={
    "name": "salmo",
    "umur": 10,
    "hobi": ["berenang", "mancing", "ngoding"],
    "pekerjaan": "mahasiswa",
    "sosmedia": {
        "instagram": "@salmo_123",
        "twitter": "@salmo_tw",
        "github": "salmo-git"
    }
}

# print("total mahasiswa: %d" % len(mhs))

# print("nama saya adalah %s, umur saya %d tahun" % (mhs["name"], mhs["umur"]))
# print(f"nama saya adalah {mhs['name']}, umur saya {mhs['umur']} tahun")

print("------------------------------------")
print("hobi saya adalah:")
for hobi in mhs["hobi"]:
    print("- %s" % hobi)

# print("------------------------------------")
# print("sosial media saya:")
# for platform, handle in mhs["sosmedia"].items():
#     print(f"{platform.capitalize()}: {handle}")

# print("------------------------------------")
# for key, value in mhs.items():
#     print(f"{key.capitalize()}: {value}")

# print("------------------------------------")
# print(mhs["hobi"])
# mhs["rutin"] = "tidur"
# print(mhs["rutin"])

# print("------------------------------------")
# print("hobi")
# mhs.pop("rutin")
# print(mhs["hobi"])

# hobi.clear()
# print("hobi setelah di clear:", hobi) = mhs["hobi"]

# mhs = {
#     "name": "salmo",
# }
# print(mhs)

# mhs.update({"email": "salmo@mail.com"})
# print(mhs)

# mhs.update({"name": "salman"})
# print(mhs)

mhs=[]
olahraga=["sepak bola", "basket", "renang"]
buku=[1234,"pemrograman dasar", True, 25]

print(buku[1])
print(f"total rak ada {format(len(buku))} rak")