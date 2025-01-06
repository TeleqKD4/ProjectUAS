```
class ProcessAkun:
    
    def __init__(self, data_akun, view_akun):
        self.data_akun = data_akun
        self.view_akun = view_akun

    def tambah_akun(self):
        akun = self.view_akun.minta_input("Masukkan nama akun: ")
        if self.data_akun.cek_akun_ada(akun):
            self.view_akun.tampilkan_pesan("Akun sudah ada.")
            return

        username = self.view_akun.minta_input("Masukkan username: ")
        password = self.view_akun.minta_input("Masukkan password: ")

        self.data_akun.tambah_data(akun, username, password)
        self.view_akun.tampilkan_pesan("Akun berhasil ditambahkan.")

    def ubah_akun(self):
        akun = self.view_akun.minta_input("Masukkan nama akun yang ingin diubah: ")
        if not self.data_akun.cek_akun_ada(akun):
            self.view_akun.tampilkan_pesan("Akun tidak ditemukan.")
            return

        username_baru = self.view_akun.minta_input("Masukkan username baru: ")
        password_baru = self.view_akun.minta_input("Masukkan password baru: ")

        self.data_akun.data[akun]["nama"] = username_baru
        self.data_akun.data[akun]["PW"] = password_baru
        self.view_akun.tampilkan_pesan("Akun berhasil diubah.")

    def hapus_akun(self):
        akun = self.view_akun.minta_input("Masukkan nama akun yang ingin dihapus: ")
        if self.data_akun.hapus_data(akun):
            self.view_akun.tampilkan_pesan("Akun berhasil dihapus.")
        else:
            self.view_akun.tampilkan_pesan("Akun tidak ditemukan.")

    def lihat_akun(self):
        self.view_akun.tampilkan_data(self.data_akun.dapatkan_data())

```
Class ini ditunjukan untuk memperoses keseluruhan semua propgram yang saling berkaitan seperti Class_view dan Class_data


