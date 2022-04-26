
# * Tanggal dan Waktu 

# ! mengimport waktu
import time ;

# ! tick menggunakan detik 
# tick = time.time()
# print("Waktu Sekarang : ", tick)

# ! Time tuple

# Mendapat waktu sekarang 

# nowtime = time.localtime();
# print("Waktu Sekarang : ", nowtime)
# # perbedaan nya dengan localtime() langsung tidak ada bedanya 
# nowtime = time.localtime(time.time());
# print("Waktu Sekarang : ", nowtime) ;

# Mendapatkan Waktu yang berformat 

# timeformat = time.asctime(time.localtime());
# print("Waktu Sekarang : ", timeformat);


# ! Kalender dalam bulan 
# mengimpor kalender 
import calendar;

cal = calendar.month(2022, 2);
print("Kalender : ", cal);
# atau cuma kalender nya tanpa mengatur bulan 
cal = calendar.calendar(2022, 2);
print("Kalender : ", cal);
