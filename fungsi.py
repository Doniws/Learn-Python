
# * Fungsi Python

# parameter 
# def print_name(name):
#     print("Hello " + name)
#     return


# def Doni():
#     print("Doni")
#     # mengembalikan nilai
#     return

# # Memanggil fungsi
# Doni();

# # loop dengan cara lama 
# Doni();
# Doni();
# Doni();

# * fungsi perulangan loop 
# def looping():
#     for i in range(1, 1000):
#         print("loop at :", i)
#     return

# ? Memanggil fungsi 
# looping();

# ! fungsi dengan menggunakan Parameter 
# def par(i):
#     print("Name :", i)
#     return

# par("Doni");


# ! latihan parameter fungsi
# def par(p , l) :
#     a = (p * l) / 2 
#     print ("Luas persegi adalah :" ,int(a) , "cm")
#     return

# memanggil dan mengisi parameternya 
# ? 10 kali 20 bagi 2
# @ p akan diisi 10 dan l akan diisi 20 
# par (10,20);

# ! Function dengan return 
# ? rumus : sisi x sisi 
# def luas_persegi(sisi):
#     luas = sisi * sisi;
#     return luas;

# luas_persegi(10);

# # ? sisi akan berubah menjadi sisi x sisi x sisi 
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     return volume

# print("Luas Persegi :,", volume_persegi(10));


# * Variable Lokal dan Global Python 

# # ! Variable Global Bisa di akses di dalam fungsi dan di luar fungsi
# nama = "Doni"
# versi = "1.0"

# def helpme():
#     # ! Ini nama Variable Local hanya bisa digunakan didalam fungsi 
#     nama = "Programku";
#     versi = "1.2"; 
#     print("Nama :", nama)
#     print("Versi :", versi)

# # ! Variable Global Bisa di akses di dalam fungsi dan di luar fungsi
# print("Nama :", nama)
# print("Versi :", versi)

# # ! local variable tidak bisa di akses di luar fungsi
# helpme(); 