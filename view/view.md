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

        print("+---------+----------+------------+")
        print("| Akun    | Username | Password   |")
        print("+---------+----------+------------+")
        for akun, info in data.items():
            print(f"| {akun:<7} | {info['nama']:<8} | {info['PW']:<10} |")
        print("+---------+----------+------------+")

```
class ini berfungsi untuk menampilkan semua program di terminal 
