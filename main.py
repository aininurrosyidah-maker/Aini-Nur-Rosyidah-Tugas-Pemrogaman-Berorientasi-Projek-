class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
    
    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")


# Membuat object mahasiswa
mahasiswa1 = Mahasiswa("Aini Rahmawati", "123456", "Teknik Informatika")
mahasiswa1.tampilkan_data()
