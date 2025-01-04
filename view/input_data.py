```
class inputakun:
    @staticmethod
    def input_akun():
        akun = input(" Masukan Nama Program ")
        username = input (" Masukan Nama Akun Program ")
        password = input (" Masukan Pasword Program")
        return akun, username, password
        
    @staticmethod
    def input_edit_akun():
        akun = input (" Masukan Nama Program")
        print(" Masukan Data Baru ( Tekan Enter Jika Tidak Ingin Mengubah Data ): ")
        username = input(" Masukan Username Akum: ")
        password = input(" Masukan Password Akun ")
        return akun, username, password
```
