#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = []
        self.total = 0
    """ Fungsi yang digunakan untuk menginisialisasi sebuah instance baru dari kelas Transaction."""
    
    def add_item(self, nama_item, jumlah_item, harga_item):
        subtotal = jumlah_item * harga_item
        self.items.append([nama_item, jumlah_item, harga_item, subtotal])
        self.total += subtotal
    """ Fungsi ini digunakan untuk menambahkan item. 
    Fungsi ini menerima tiga parameter: 
    - nama_item (string) : nama item/barang yang akan ditambahkan customer
    - jumlah_item (integer) : jumlah item/barang yang diinputkan customer
    - harga_item (float) : harga per item/barang
    Selain itu, fungsi ini menghitung subtotal dari item tersebut dan menambahkannya ke parameter total. 
    Item yang ditambahkan disimpan dalam bentuk list [nama_item, jumlah_item, harga_item, subtotal]."""

    def update_item_name(self, nama_item, nama_item_baru):
        for item in self.items:
            if item[0] == nama_item:
                item[0] = nama_item_baru
                break
    """ Fungsi ini digunakan untuk update nama item. Nama item yang lama akan diganti dengan nama item baru (update)"""
    
    def update_item_quantity(self, nama_item, jumlah_item_baru):
        if len(self.items) == 0:
            print("Tidak ada item yang tersedia untuk diperbarui.")
            return
        
        for item in self.items:
            if item[0] == nama_item:
                item[1] = jumlah_item_baru
                item[3] = item[1] * item[2]
                break
    """ Fungsi ini digunakan untuk update jumlah item, inputkan nama item yang akan diupdate jumlah itemnya."""
    
    def update_item_price(self, nama_item, harga_item_baru):
        if len(self.items) == 0:
            print("Tidak ada item yang tersedia untuk diperbarui.")
            return
        
        for item in self.items:
            if item[0] == nama_item:
                item[2] = harga_item_baru
                item[3] = item[1] * item[2]
                break
    """ Fungsi ini digunakan untuk update harga per jumlah item, inputkan nama item yang akan diupdate harga itemnya."""
                   
    def delete_item(self, nama_item):
        for item in self.items:
            if item[0] == nama_item:
                self.total -= item[3]
                self.items.remove(item)
                break
        else:
            print("Item tidak ditemukan. Masukkan nama item dengan benar!")
    """ Fungsi ini digunakan untuk menghapus salah satu item yang telah kita pilih nama itemnya"""

    def reset_transaction(self):
        if len(self.items) == 0:
            msg = "Sebelumnya anda tidak memiliki list item."
            print("+" + "-" * (len(msg) + 2) + "+")
            print("|", msg, "|")
            print("+" + "-" * (len(msg) + 2) + "+")
        else:
            self.items.clear()
            msg = "Seluruh item berhasil dihapus, anda tidak memiliki item dalam pesanan anda."
            print("+" + "-" * (len(msg) + 2) + "+")
            print("|", msg, "|")
            print("+" + "-" * (len(msg) + 2) + "+")
    """ Fungsi ini digunakan untuk menghapus seluruh item yang telah diinputkan."""
    
    def total_price(self):
        if len(self.items) == 0:
            msg = "Anda tidak memiliki item untuk dibayar."
            print("+" + "-" * (len(msg) + 2) + "+")
            print("|", message, "|")
            print("+" + "-" * (len(msg) + 2) + "+")
     
        else:
            total = 0
            for item in self.items:
                total += item[3]
            total_belanja = "Rp.{:.0f}.{:03.0f},-".format(total // 1000, total% 1000)
            print("Total:", total_belanja)
            
            diskon_1 = "Rp.{:.0f}.{:03.0f},-".format((total * 0.95) // 1000, (total * 0.95) % 1000)
            diskon_2 = "Rp.{:.0f}.{:03.0f},-".format((total * 0.92) // 1000, (total * 0.92) % 1000)
            diskon_3 = "Rp.{:.0f}.{:03.0f},-".format((total * 0.9) // 1000, (total * 0.9) % 1000)
            if total > 200000:
                print("Selamat anda Anda mendapatkan diskon 5%")
                print("Total belanja yang harus anda bayar : ", diskon_1)
            elif total > 300000:
                print("Selamat anda Anda mendapatkan diskon 8%")
                print("Total belanja yang harus anda bayar : ", diskon_2)
            elif total > 500000:
                print("Selamat anda Anda mendapatkan diskon 10%")
                print("Total belanja yang harus anda bayar : ", diskon_3)
            else:
                print("Total belanja yang harus anda bayar : ", total_belanja)           
    """ Fungsi ini digunakan untuk menghitung total harga yang harus dibayar customer"""               
    
    def check_order(self):      
        if len(trnsct_123.items) == 0:
            print("Tidak ada item dalam pesanan Anda.")
        else:
            tabel_transaksi = trnsct_123.items
            headers = ["Nama Item", "Jumlah Item", "Harga", "Subtotal"]
            table = tabulate(tabel_transaksi, headers, tablefmt="grid")
            print(table)
        """ Fungsi ini digunakan untuk menampilkan tabel order nama item yang telah diinput."""

        
trnsct_123 = Transaction()
print("Selamat datang di program super cashier!")
customer_id = input("Masukkan ID transaksi Anda: ")

while True:
    print("Silakan pilih menu:")
    print("1. Tambah item")
    print("2. Update nama item")
    print("3. Update jumlah item")
    print("4. Update harga item")
    print("5. Delete item")
    print("6. Reset Transaction")
    print("7. Cek Order")
    print("8. Hitung total")
    print("9. Keluar")
    
    menu = int(input("Masukkan pilihan Anda: "))
    
    if menu == 1:
        while True:
            while True:
                nama_item = input("Masukkan nama item: ")
                nama_item_clean = nama_item.strip()
                if (not nama_item.strip()) or (nama_item.isspace()) or (nama_item==""):
                    print("Nama item tidak boleh kosong. Silakan masukkan nama item dengan benar.")
                else:
                    break

            while True:
                try:
                    jumlah_item = int(input("Masukkan jumlah item: "))
                    break
                except ValueError:
                    print("Jumlah item harus berupa angka. Silakan masukkan jumlah item dengan benar.")
            
            while True:
                try:
                    harga_item = float(input("Masukkan harga item: "))
                    break
                except ValueError:
                    print("Harga item harus berupa angka. Silakan masukkan harga item dengan benar.")
            
            trnsct_123.add_item(nama_item_clean, jumlah_item, harga_item)
            trnsct_123.check_order()

    
            while True:
                pilihan = input("Tambah item lagi? (Y/N): ")
                if pilihan.lower() == "n":
                    break
                elif pilihan.lower() == "y":
                    break
                else:
                    print("Masukkan pilihan dengan benar!")
            if pilihan.lower() == "n":
                break
            elif pilihan.lower() == "y":
                continue
                                                                   
    elif menu == 2:
        if len(trnsct_123.items) == 0:
            print("Tidak ada item yang tersedia untuk diperbarui.")
                
        nama_item = input("Masukkan nama item yang akan diperbarui: ")
        nama_item_clean = nama_item.strip()
        nama_item_baru = input("Masukkan nama item baru: ")
        nama_item_baru_clean = nama_item_baru.strip()
        
        trnsct_123.update_item_name(nama_item_clean, nama_item_baru_clean)
        trnsct_123.check_order()
        
    elif menu == 3:
        nama_item = input("Masukkan nama item yang akan diperbarui: ")
        while True:
            try:
                jumlah_item_baru = int(input("Masukkan jumlah item baru: "))
                break
            except ValueError:
                print("Jumlah item harus berupa angka. Silakan masukkan jumlah item dengan benar.")
        trnsct_123.update_item_quantity(nama_item, jumlah_item_baru)
        trnsct_123.check_order()
        print("Jumlah item berhasil diperbarui.")
        
    elif menu == 4:
        nama_item = input("Masukkan nama item yang akan diperbarui: ")
        while True:
            try:
                harga_item_baru = float(input("Masukkan harga item baru: "))
                break
            except ValueError:
                print("Harga item harus berupa angka. Silakan masukkan harga item dengan benar.")
        trnsct_123.update_item_price(nama_item, harga_item_baru)
        trnsct_123.check_order()
        print("Harga item berhasil diperbarui.")
        
    elif menu == 5:
        if len(trnsct_123.items) == 0:
            print("Tidak ada item yang dapat dihapus.")
        else:
            nama_item = input("Masukkan nama item yang akan dihapus: ")
            trnsct_123.delete_item(nama_item)
            trnsct_123.check_order()
            print(f"Item '{nama_item}' berhasil dihapus.")
 
    elif menu == 6:
        # Hapus semua item
        if len(trnsct_123.items) == 0:
            print("Tidak ada item yang dapat dihapus.")
        else:
            trnsct_123.reset_transaction()
            trnsct_123.check_order()
              
    elif menu == 7:
        print("Berikut adalah daftar belanjaan anda :)")
        trnsct_123.check_order()
        
        pilihan = input("Kembali ke menu? (Y/N): ")
        if pilihan.lower() == "n":
            trnsct_123.total_price()        
            pilihan = input("Apakah anda sudah selesai berbelanja? (Y/N): ")
            if pilihan.lower() == "y":
                print("Terima kasih telah berbelanja :)")
                break
            elif pilihan.lower() == "n":
                continue
            else:
                while pilihan.lower() not in ["y", "n"]:
                    pilihan = input("Tambah item lagi? (Y/N): ")
                if pilihan.lower() == "y":
                    break

        elif pilihan.lower() == "y":
            continue
        else:
            while pilihan.lower() not in ["y", "n"]:
                pilihan = input("Tambah item lagi? (Y/N): ")
            if pilihan.lower() == "n":
                break

    elif menu == 8:
        trnsct_123.check_order()
        trnsct_123.total_price()
        print("Terima kasih telah berbelanja :)")
        
        pilihan = input("Kembali ke menu? (Y/N): ")
        if pilihan.lower() == "n":
            break
        elif pilihan.lower() == "y":
            continue
        else:
            while pilihan.lower() not in ["y", "n"]:
                pilihan = input("Kembali ke menu? (Y/N): ")
            if pilihan.lower() == "n":
                break 

    elif menu == 9:
        print("Terima kasih telah berbelanja :)")
        break
    else:
        print("Pilihan tidak valid!")
        
    """
    - Menu pilihan pertama akan memanggil fungsi add_item dan check_order untuk menampilkan item apa saja yang telah diinput 
    oleh customer dalam bentuk table. Saat customer melakukan input nama item, jumlah item dan harga item
    tidak boleh dalam keadaan kosong harus melakukan input dengan benar. Ketika inputan dalam keadaan kosong maka
    program akan meminta customer untuk melakukan inputan secara benar.
    Setelah customer melakukan input nama item, jumlah item dan harga item, maka customer akan dihadapkan pada pilihan
    tambah item atau kembali ke menu utama di awal.

    - Menu pilihan kedua akan memanggil fungsi update_item_name dan check_order
    
    - Menu pilihan ketiga akan memanggil fungsi update_item_quantity dan check_order
    
    - Menu pilihan keempat akan memanggil fungsi update_item_price dan check_order
        
    - Menu pilihan kelima akan memanggil fungsi delete_item dan check_order
    
    - Menu pilihan keenam akan memanggil fungsi reset_transaction dan check_order

    - Menu pilihan ketujuh akan memanggil fungsi check_order. Setelah tampil tabel transaksi,
    customer akan memiliki pilihan untuk kembali ke menu atau tetap ada di menu check_order, jika memilih no maka akan tampil
    total harga yang perlu dibayar. Setelah tampil total harga yang perlu dibayar, customer akan memilih kembali untuk lanjut
    belanja atau tidak. Jika lanjut maka akan kembali ke menu utama di awal, namun jika tidak lanjut maka program berhenti.
    
    - Menu pilihan kedelapan memanggil total_price dan check_order. Setelah tampil tabel transaksi dan total harga,
    customer akan memilih kembali ke menu utama atau tidak. Jika memilih tidak maka program berhenti.
    """


# In[ ]:





# In[ ]:





# In[ ]:




