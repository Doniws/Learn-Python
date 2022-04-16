# Python Program

# * Latihan variable dan memanggil nya
# nama = "Doni ws"
# umur = 16;
# print("Nama Saya : ", nama ,"\n","Umur Saya : ", umur)


# print("Nama : ", nama ,"\n","Umur : ", umur)
# type(nama)
# type(umur)

# Front_name = "Doni"
# Back_name = "Ws"
# umur = 16
# hobi = "Sleep Every Time"
# nama = Front_name + " " + Back_name
# print("Biodata\n", "My name : ", nama, "\n",
#       "My Age : ", umur, "\n", "My Hobi : ", hobi)

# *Operator Python
# +, -, *, /, //, **, %
# P = 10.3
# L = 5.44
# # pembagian
# print(P / L);
# # pembagian Pembulatan
# print(P // L);
# # pangkat
# print(P ** L);
# # sisa bagi
# print(P % L);

# * Operator Pembanding
# ==, !=, >, <, >=, <=
# Tidak Sama Dengan
# print(10 != 1)
# # Lebih Besar Dari
# print(10 > 1)
# # Lebih Kecil Dari
# print(10 < 1)
# # Lebih Besar Dari Atau Sama Dengan
# print(10 >= 1)
# # Lebih Kecil Dari Atau Sama Dengan
# print(10 <= 1)


# * if else
# nilai = 80
# if nilai >= 80:
#     print("Selamat, Anda Lulus")
# else:
#     print("Maaf, Anda Tidak Lulus")

# ! Perbedaan >= dengan >
# >= saat nilai itu pas
# > saat nilai itu tidak pas atau melebihi nilai ynag ditentukan

# * if else banyak
# now_day = "sunda2y"
# if now_day == "sunday":
#     print("Lazy Time")
# elif now_day == "monday":
#     print("Work Time")
# elif now_day == "tuesday":
#     print("Study Time")
# elif now_day == "wednesday":
#     print("Work Time")
# elif now_day == "thursday":
#     print("Study Time")
# elif now_day == "friday":
#     print("Work Time")
# elif now_day == "saturday":
#     print("Today is saturday")
# else:
#     print("Today is not a day")

# * Perulangan While
# count = 0
# while count < 10:
#     print("loop at :", count)
#     count  = count + 1

# * Perulangan For
# for i in range(1, 10):
#     print("loop at :", i)

# Perulangan Berdasarkan array
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in angka:
#     print("loop at :", i)

# makanan = ["Nasi Goreng", "Soto", "Sate", "Bakso", "Nasi Padang"]
# for i in makanan:
#     print("  Saya sukan makan :", i)

# ! Percabangan Bersarang
# i = 2
# while(i < 100):
#     j = 2
#     while(j <= (i/j)):
#         if not(i % j):
#             break
#         j = j + 1
#     if (j > i/j):
#         print(i, " is prime")
#     i = i + 1


# * String Python
# makanan = "Nasi Goreng", " Soto", " Sate", " Bakso", " Nasi Padang"
# makanan2 = "Telur"
# (1:2) maksudnya untuk mengakses index ke 1 sampai ke 2
# jika itu array dia akan mengakses perkata , jika bukan array dia hanya akan mengakses katanya saja
# print(makanan[2:5])
# print(makanan2[2:6])

#  ! + dalam python menambahkan suatu string atau pun angka
# message = 'Hello World'
# print("Updated String :- ", message[:6] + 'Python')

# * List Python

# pelajaran = ["Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Inggris"]
# pelajaran2 = ["b ind ", 22, 23, "bakso"]


# ! Cara mengakses nilai di dalam list Python

# list1 = ['fisika', 'kimia', 1993, 2017]
# ! digunakan untuk memisah kan suatu kata
# list2 = [1, 2, 3, 4, 5, 6, 7]

# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[4:5])

# list = ["fisika", "kimia", 1993, 2017]
# # menambahkan math menggunakan append
# list.append("Math")
# print("list[1]: ", list[1])

# # update di python
# list[1] = 80
# # Merubah kimia Menjadi 80
# print("Kimia Menjadi 80 : ",list[1])

# # Menghapus List dalam Python
# print(list)
# del list[2]
# print("1993 di hapus dari list : ", list)

# # Menghuitung jumlah object  count
# print("fisika ada sebanyak : ", list.count("fisika"))

# * Menggunakan Tuple di python hampir mirip dengan list
# tup = ("Sleep", "Eat", "Code", 2022, 2024)

# print(tup)

# menghitung panjang tup
# print("Panjang tup : ", len(tup))

# mengakses kata di dalam tuple
# print("Kata di dalam Tuple : ", tup[2])
# print("Hanya Beberapa Kata : ", tup[0:3])

# ! Update Tuple
# tup1 = ("C++" , "Java", "Python", "C#", "JavaScript")
# tup2 = (2021, 2022, 2023, 2024, 2025)

# tuple tidak bisa di ubah seperti ini
# tup1[0] = 2021

# buat tuple baru untuk mengubahnya
# tup3 = tup1 + tup2
# print(tup3)


# ! Hapus Tuple
# tup = ("Sleep", "Eat", "Code", 2006, 2060)
# print("Tup yang di Hapus : ", tup)

# tup akan terhapus dan tidak bisa di akses lagi
# del tup

# membuat tup baru
# tup = ("School", "Work", "Code", 2022, 2024)
# print("Tup Baru : ",tup)


# # ? Mengalikan Tuple
# tup = ("Hello",) * 4
# print("Tuple : ", tup)


# ! Perbedaan Tuple dan List :
# Tuple Menggunakan () dan List Menggunakan [] , Tuple tidak bisa diubah dan List bisa diubah
