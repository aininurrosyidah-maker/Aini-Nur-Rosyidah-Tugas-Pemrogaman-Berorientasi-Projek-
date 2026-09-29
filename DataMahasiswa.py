class Mahasiswa:
    def __init__(self, nama, nim, prodi, ipk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.ipk = ipk

    def cek_status(self):
        if self.ipk >= 3:
            return "Lulus"
        else:
            return "Tidak Lulus"
    def tampilkan_info(self):
        status = self.cek_status()
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("IPK:", self.ipk)
        print(status)
        print()

mhs1 = Mahasiswa("Andi Pratama", "23101125001", "Teknik informatika", 3)
mhs2 = Mahasiswa("Sinta Maharani Putri", "23102125002", "Teknik Informatika", 2)
mhs3 = Mahasiswa("Aulia Rahma Putri", "231031003", "Sistem Informasi", 4 )
mhs1.tampilkan_info()
mhs2.tampilkan_info()
mhs3.tampilkan_info()