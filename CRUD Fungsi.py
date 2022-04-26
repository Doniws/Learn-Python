
# * Latihan Membuat crud py3

# ? array buku kosong = [] 
# ? dibagian edit ada yang error dan sedang dalam perbaikan 

buku = []

# * Menampilkan data 
def show_data():
    if len(buku) <= 0:
        print("Data Kosong")
    else:
        print("Data buku :")
        for i in range(len(buku)):
            print(i + 1, ". ", buku[i])

# * Memasukan Data dengan Input 
def insert_data():
    buku_baru = input("Masukan judul buku : ")
    buku.append(buku_baru)

# * Mengedit data 
def edit_data():
    show_data();
    i = input("Masukan indeks yang akan di edit : ")
    if i > len(buku): # @ error
        print("Data tidak ada")
    else:
        judul_baru = input("Masukan judul buku baru : ")
        buku[i] = judul_baru;
        print("Data telah di edit")

# * Menghapus data 
def delete_data():
    show_data();
    i = input("Masukan indeks yang akan di hapus : ");
    if i >= len(buku):
        print("Data tidak ada")
    else:
        buku.remove(buku[i])

# * Menu 
def show_menu():
    print("\n")
    print("Pilih menu :")
    print("1. Tampilkan data")
    print("2. Input data")
    print("3. Edit data")
    print("4. Delete data")
    print("5. Exit")
    
    menu = input("Pilih menu : ")
    print("\n")

    if menu == "1":
        show_data();
    elif menu == "2":
        insert_data();
    elif menu == "3":
        edit_data();
    elif menu == "4":
        delete_data();
    elif menu == "5":
        print("Terima kasih telah menggunakan program ini")
        exit();

if __name__ == "__main__":

    while(True):
        show_menu()