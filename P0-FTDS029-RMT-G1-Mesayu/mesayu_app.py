print("==================================")
print("Nama     : Mesayu Gina Puspita")
print("Batch    : RMT-029")
print("Program ini dibuat untuk melakukan automatisasi pengolahan (cleaning) data text yang berguna untuk pemodelan model analisa sentimen")
print("==================================")


class chartitem: # membuat class chartitem
    def __init__(self, nama, harga): # Menginisialisasi variabel input
        self.nama = nama
        self.harga = harga
    
    def __str__(self):
        return f"{self.nama} - {self.harga}"
    
item1 = chartitem("apel", 3400)
item2 = chartitem("jeruk", 2100)  

print(item1)
print(item2)



class shoppingcart: # Membuat class shoppingcart
    def __init__(self):
        self.item = []

    def tambah_barang(self, item):
        self.item.append(item)

    def hapus_barang(self, nama_item):
        for item in self.item:
            if item.nama == nama_item:
                self.item.remove(item)
                print("barang sudah dihapus dari keranjang")
                return
        print("barang tidak ditemukan di keranjang")
    
    def total_belanja(self):
        total = sum(harga for item in self.item)
        return total
    
    def user_interface(self):
        while True:
            print("menu:")
            print("1. Menambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang di keranjang")
            print("4. Total belanja")
            print("5. Exit")

            pilihan = input("pilihan:")

            if pilihan == 1:
                nama_barang = input('masukan nama barang :') 
                harga_barang = float(input('masukan harga:'))
                item = chartitem(nama_barang, harga_barang)
                self.tambah_barang(item)
            elif pilihan == 2:
                nama_barang = input("masukan nama barang yang di hapus")
                self.hapus_barang(nama_barang)
            elif pilihan == 3:
                nama_barang = input('tampilkan barang di keranjang')
                for index, item in enumerate(self.items):
                    print(f"{index}. {item}")
            elif pilihan == 4:
                total = self.total_belanja()
                print(f"Total belanja: Rp {total:}")
            elif pilihan == 5:
                print('Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur')
                break
            else:
                print('pilihan salah, silahkan dicoba kembali')

keranjang = shoppingcart()   
keranjang.user_interface()  