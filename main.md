```
from data.akun import Akun
from view.input_data import inputakun
from view.akun import view_akun 

def main ():
    akun = Akun ()
    while True:
        Pilihan = input ("[L]ihat [T]ambah [E]dit [H]apus [K]eluar: "). lower()
        if Pilihan == 'l':
            view_akun.tampilkan_data(akun)
        elif Pilihan == 't':
            akun, username, password = inputakun.input_akun()
            akun.tambah_akun (akun, username, password)
        elif Pilihan == 'e':
            akun, username, password = inputakun.input_edit_akun()
            akun.edit_akun (akun, username, password)
        elif Pilihan == 'h':
            akun = input( "Masukan nama Program yang ingih di hapus akunnya: ")
            akun.hapus_data(akun)
        elif Pilihan == 'k':
            print(" Program Selesai")
            break
        else:
            print(" pilihan tidak valid! ")

if __name__ == "__main__":
    main()
```
