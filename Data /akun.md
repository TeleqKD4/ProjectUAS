```
class Akun:
    def __init__(self):
        self.data_akun = {}
        
    def lihat_data(self):
        if not self.data_akun:
            print(" Daftar Akun ")
            print("=" * 81)
            print(f"{'No'.center(5)}|{'Akun'.center(15)}|{'Username'.center(10)}|{'Password'.center(13)}|")
            print("=" * 81)
            print(f"{'TIDAK ADA DATA'.center(75)}")
            print("=" * 81)
            return
        print("Daftar Nilai")
        print("=" * 81)
        print(f"{'No'.center(5)}|{'Akun'.center(15)}|{'Username'.center(10)}|{'Password'.center(13)}|")
        print("=" * 81)
        for i, (Akun,Username, password) in enumerate(self.data_akun.items(), start=1):
            print(f"{str(i).center(5)}|{Akun['nama aplikasi'].ljust(15)}|{Username.center(10)}|{str(password ['password']).center(13)}|")
        print("=" * 81)
    
    def tambah_akun(self, akun, username, password):
        self.data_akun [akun]={
            "akun":akun,
            "nama":username,
            "PW":password
        }
    def edit_akun(self, akun, username=None, pasword=None):
        if akun not in self.data_akun:
            print("anda tidak memliki akun di software tersebut")
            return
        if username :
            self.data_akun [username] ["nama"] = username  
        if pasword is not None :
            self.data_akun [pasword] ["PW"] = pasword
            
    def hapus_data (self, akun) :
        if akun in self.data_akun:
            del self.data_akun [akun]
            print("Data Akun Berhasil di Hapus")
        else :
            print("Anda Tidak Mempunyai Akun di Program Tersebut")
    ```
