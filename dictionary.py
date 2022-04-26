
# * Dictionary Python

# ! disct menggunakan {} untuk membuat dictionary 
# dict = {"Doni" : "sate ", "Niken" : "nasi goreng", "Lur" : "soto"}
# # untuk mengakses dict harus menggunakan key 
# print("Doniws ", dict["Doni"])
# print("Lur",dict['Lur'])

# # @ Mengupdate Dictionary 
# dict['Doni'] = "Nasi Padang"

# ! Menghapus Dictionary 
# @ menghapus dict yang dipilih 
# del dict['Doni']
# print(dict)

# @ Menghapus semua dict yang ada 
# dict.clear()
# print(dict)

# @ menghapus semua dict sampai tidak tersisa 
# del dict
# print(dict)

# * Dictionary Python Latihan 
# nama_dict = {
#     "Doni" : "sate",
#     "Niken" : "nasi goreng",
#     "Lur" : "soto"
# }

 # *  Dict bercabang  
Doni = {
    "Nama" : "Doni",
    "Kelas" : "Smk 10",
    "Alamat" : "Kemnadoran 8",
    "Social Media" : {
        "Facebook" : "Doniws",
        "Instagram" : "Doni",
        "Twitter" : "Doni"
    }
}

# @ Mengakses nilai datlam dict  
# print(Doni['Social Media']['Facebook'])

# @ Mencentak Perulangan Dict 
for i in Doni:
    print(Doni[i])

# * atau juga bisa jika menggunakan ini kurung kurawal akan hilang {}
for key, value in Doni.items():
    print(key, value)

# * Mengecek panjang directry 
print(len(Doni))

# * Selain Menggunakan Seperti diatas 
# @ Bisa Gunakan dict()

# Doni_stats = dict( nama = "Doni", kelas = "Smk 10", alamat = "Kemnadoran 8",)
# print(Doni_stats)

