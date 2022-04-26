
# * time

import time 

# time.sleep(2)
# print("Akan Memulai Program Dalam 2 Detik")

# * Latihan 

# Perulangan while dengan time 
# ! Membuat jam real time dengan jeda setiap 1 detik 
# while True :
#     waktu = time.localtime()
#     # @ Akan menampilan semua ms sampai hour 
#     # print(waktu)
#     # @ Akan menampilkan hour , minute , second tapi tanpa keterangan pm atau am
#     # print(waktu.tm_hour , ":" , waktu.tm_min , ":" , waktu.tm_sec)
#     # @ Akan menampilkan hour , minute , second dan keterangan pm atau am
#     result = time.strftime("%I:%M:%S %p")
#     print(result)
#     # @ Memperbarui waktu setiap 1 detik 
#     time.sleep(1)
#     print("\n")

# * Latihan 2 

# * Multithreading 

import threading

# def multi_hello() :
#     # @ loop 10 kali
#     for i in range(11) :
#         print("Hello")

# def multi_hai() :
#     for i in range(11) :
#         print("Hai")

# # @ Memanggil threading untuk membuat thread
# m1 = threading.Thread(target = multi_hello)
# m2 = threading.Thread(target = multi_hai)

# # ! Memanggil m1 dan m2 
# m1.start()
# m2.start()


# * Latihan 3
# * Menggabungan Threading dan time 

def multi_hello() :
    # @ loop 10 kali
    for i in range(11) :
        # @ Mengkombinasikan dengan sleep time 
        time.sleep(0.5)
        print("Hello")

def multi_hai() :
    for i in range(11) :
        time.sleep(1)
        print("Hai")

# @ Memanggil threading untuk membuat thread
m1 = threading.Thread(target = multi_hello)
m2 = threading.Thread(target = multi_hai)

# ! Memanggil m1 dan m2 
m1.start()
m2.start()

