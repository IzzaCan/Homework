import homework as ds
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def daftar_menu():
    while True:
        clear_screen()

        print("Selamat Datang Di Program Manajemen Stok Barang")
        print("\n=====Daftar Menu=====")
        print("1. Tambah Data Barang")
        print("2. Edit Data Barang")
        print("3. Hapus Data Barang")
        print("4. Cari Data Barang")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Barang")
        print("7. Keluar")

        menu = input("Masukkan pilihan : \n")

        clear_screen()
        
        if menu == '1':
            ds.insert_data()
        elif menu == '2':
            ds.edit_data()
        elif menu == '3':
            ds.delete_data()
        elif menu == '4':
            ds.search_data()
        elif menu == '5':
            ds.show_data()
        elif menu == '6':
            ds.show_amount()
        elif menu == '7':
            exit()
        else:
            print("Salah pilih!")

        input("\nTekan Enter untuk kembali ke menu.")

daftar_menu()
