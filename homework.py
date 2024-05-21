data_barang = []

def insert_data():
    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    barang = {
        "nama": nama_barang,
        "jumlah": jumlah_barang
    }
    
    data_barang.append(barang)
    print("Data barang berhasil ditambahkan!")

def edit_data():
    nama_barang = input("Masukkan nama barang yang akan diedit: ")
    
    for barang in data_barang:
        if barang["nama"] == nama_barang:
            print(f"Data lama: {barang}")
            barang["jumlah"] = int(input("Masukkan jumlah barang baru: "))
            print("Data barang berhasil diubah!")
            return
    
    print("Barang tidak ditemukan!")

def delete_data():
    nama_barang = input("Masukkan nama barang yang akan dihapus: ")
    
    for barang in data_barang:
        if barang["nama"] == nama_barang:
            data_barang.remove(barang)
            print("Data barang berhasil dihapus!")
            return
    
    print("Barang tidak ditemukan!")

def search_data():
    nama_barang = input("Masukkan nama barang yang dicari: ")
    
    for barang in data_barang:
        if barang["nama"] == nama_barang:
            print(f"Data barang ditemukan: {barang}")
            return
    
    print("Barang tidak ditemukan!")

def show_data():
    if data_barang:
        print("Daftar Data Barang:")
        for barang in data_barang:
            print(barang)
    else:
        print("Tidak ada data barang!")

def show_amount():
    jumlah_total = sum(barang["jumlah"] for barang in data_barang)
    print(f"Jumlah total barang: {jumlah_total}")