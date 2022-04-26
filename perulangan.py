
# * Perulangan While
count = 0
while count < 10:
    print("loop at :", count)
    count  = count + 1

# * Perulangan For
for i in range(1, 10):
    print("loop at :", i)

# Perulangan Berdasarkan array
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in angka:
    print("loop at :", i)

makanan = ["Nasi Goreng", "Soto", "Sate", "Bakso", "Nasi Padang"]
for i in makanan:
    print("  Saya sukan makan :", i)

# ! Percabangan Bersarang
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i % j):
            break
        j = j + 1
    if (j > i/j):
        print(i, " is prime")
    i = i + 1