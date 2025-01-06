```
class ViewAkun:

    @staticmethod
    def minta_input(prompt):
        return input(prompt)

    @staticmethod
    def tampilkan_pesan(pesan):
        print(pesan)

    @staticmethod
    def tampilkan_data(data):
        if not data:
            print("Tidak ada data akun yang tersedia.")
            return

        print("-"* 60)
        print(f"|{'Akun':<10} | {'Username':<15} | {'Password':<15} |")
        print("-"* 60)
        for akun, info in data.items():
            print(f"| {akun:<10} | {info['nama']:<15} | {info['PW']:<15} |")
        print("-"* 60)

```
class ini berfungsi untuk menampilkan semua program di terminal 
