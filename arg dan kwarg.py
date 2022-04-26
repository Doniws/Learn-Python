
# *arg dan **kwarg 
# @ Arg itu tuple sedangkan kwarg itu dictionary 
# ! Ini digunakan sebagai parameter dalam fungsi
# ? jika digunakan di variable maka akan error 

# @ arg 
# def halo(*hai) :
#     print("Greeting to : ")
#     for i in hai:
#         print (i)

# halo("Doni", "Dwi", "Dian")
# ! Sudah tidak perlu Print Karena Sudah ada di dalam fungsi i in hai

# ? Arg dan kwarg digunakan untuk parameter fungsi yang tidak pasti 

# def nama(nama1 , nama2 , nama3) :
#     print("Greeting to : ")
#     print(nama1)
#     print(nama2)
#     print(nama3)

# ! ini hanya mampu menerima 3 parameter saja 
# nama("Doni", "Dwi", "Dian")
# jika melebihi jumlah Parameter maka akan error

# @ maka dari itu harus menggunakan arg dan kwarg
# ! percobaan kwarg 
# @ saat menggunakan kwarg harus menyertakan 
# coba(nama = "Doni")

# def pesan(**pesan) :
#     print(pesan)

# # ? Hasil ny akan menjadi dictionary 
# pesan(nama = "Doni", umur = "20", pekerjaan = "Pelajar")


# ! Perbedaan arg dan kwarg
# def arg(*arg) :
    # print(arg)

# ? Hasil akan berubah menjadi tuple 
# print(1,2,3)

# def kwarg(**kwarg) :
#     print(kwarg)

# ? Hasil akan berubah menjadi dictionary 
# kwarg(kwarg1 = 1 , kwarg2 = 2 , kwarg3 = 3)

# @ atau juga bisa memanggil fungsi dengan ini 

# @ siapkan parameternya
# list_nomer = [123, 888, 4444]
# isi_sms = {'tujuan': 4444, 'pesan': 'mau daftar pak'}

# ! Ada Kesalahan di sini^
# pemanggilan fungsi
# kirim_sms(*list_nomer)
# tulis_sms(**isi_sms)

# * Latihan

def nilai(*nilai) :
    # @ Mengecek Jumlah Siswa 
    banyak_siswa = len(nilai)
    # @ Menambah Semua Nilai
    jumlah_nilai = sum(nilai)
    rata_rata = float(jumlah_nilai) / float(banyak_siswa)
    return rata_rata

# ? Mengisi Sekaligus Memanggil Fungsi  
print(nilai(10,20,30,40,50))