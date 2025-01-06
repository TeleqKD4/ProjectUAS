```
class DataAkun:
    """Class untuk menyimpan data akun."""
    def __init__(self):
        self.data = {}

    def tambah_data(self, akun, username, password):
        self.data[akun] = {"nama": username, "PW": password}

    def hapus_data(self, akun):
        if akun in self.data:
            del self.data[akun]
            return True
        return False

    def cek_akun_ada(self, akun):
        return akun in self.data

    def dapatkan_data(self):
        return self.data

```
class ini di gunakan untuk menyimpan semeua data yang telah di input bahkan anda sebagi user dapat menambah data baru mengubah data dan menghapus data. jadi intinya class data ini berfungsi sebagai tembpat penyimpanan dari data-data yang telah di input di program
