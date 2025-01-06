```
from data.data import DataAkun
from view.view import ViewAkun
from process.process import ProcessAkun

def main():
    data_akun = DataAkun()
    view_akun = ViewAkun()
    process_akun = ProcessAkun(data_akun, view_akun)

    while True:
        print("\nMenu:")
        print("1. Lihat Akun")
        print("2. Tambah Akun")
        print("3. Ubah Akun")
        print("4. Hapus Akun")
        print("5. Keluar")
        pilihan = view_akun.minta_input("Pilih menu: ")

        if pilihan == "1":
            process_akun.lihat_akun()
        elif pilihan == "2":
            process_akun.tambah_akun()
        elif pilihan == "3":
            process_akun.ubah_akun()
        elif pilihan == "4":
            process_akun.hapus_akun()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
```
untuk main ini merupakan file untuk mengeksekusi seluruh program ini atau bisa di bilang tempat untuk ngerun nya seluruh program ini dan program hanya bisa jalan jika di runnyadi fike ini yaitu main.
