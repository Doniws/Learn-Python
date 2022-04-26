
# @ max() akan Mengambil nilai terbesar dari list
# @ min() akan Mengambil nilai terkecil dari list
# bulan = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}
# tmp = min(bulan["January"] , bulan["February"] , bulan["March"] , bulan["April"] , bulan["May"] , bulan["June"] , bulan["July"] , bulan["August"] , bulan["September"] , bulan["October"] , bulan["November"] , bulan["December"])
# print(tmp)


# * Latihan max dan min Mencari Nilai Terbesar dan Terkecil

print("Python Nilai Ulangan Menghitung Rata - rata Nilai ujian ")
print("===========================================================")
print("" , 100)

nilai = {"Doni": 100 , "Dwi": 80 , "Dian": 70 , "Dani": 60 , "Dino": 50}

for e in nilai :
    nilai[e] = input("Masukan Nilai Ujian " + e + " : ")

# @ Mencari nilai tertinggi 
rank = max(nilai["Doni"] , nilai["Dwi"] , nilai["Dian"], nilai["Dino"])

# @ cari dan mencetak nilai 
for e in nilai :
    if nilai[e] == rank :
        print("Nilai Tertinggi : " + e + " dengan nilai " + str(nilai[e]))




