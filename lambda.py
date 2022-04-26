# * Lambda Expression atau Anonymous Function
# ? lambda adalah sebuah fungsi yang hanya dapat dijalankan sekali
# salam = lambda nama : print("Hello World",{nama})

# @ memanggil 2 anoymous atau lambda 
# hai = salam 
# ! nama akan berubah menjadi doni 
# salam("Doni")
# hai("Niken")

# ! test operator 
# volume_persegi = lambda sisi : sisi * sisi * sisi

# print(volume_persegi(10))


# * LAMBDA SECARA LANGSUNG 
# (lambda x,y: x**2 + y**2)(4,6)
# # @simpan dalam variable
# hasil = (lambda x,y: x**2 + y**2)(4,6)

# print(hasil)

bilangan = [10,2,8,7,5,4,3,11,0, 1]
# @ map akan menjadi lambda expression
filtered_result = map (lambda x: x*x, bilangan) 
print(list(filtered_result))

