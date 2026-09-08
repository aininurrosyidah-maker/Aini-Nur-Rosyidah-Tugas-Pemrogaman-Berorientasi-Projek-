class Mahasiswa:
    def __init__(self, nama, nim, prodi, semester, ipk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi 
        self.semester = semester
        self.ipk = ipk

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("Semester:", self.semester)
        print("IPK:", self.ipk)
        print ("-----------------------------")
        

mhs1 = Mahasiswa("Andi Hermawan", "2222", "Teknik Informatika", "3", "3.78")
mhs2 = Mahasiswa("Sinta Amelia", "2223", "Teknik Elektro", "4", "3.92")
mhs3 = Mahasiswa("Lyla Anjani", "2224", "Teknik Kimia", "5", "3.82")
mhs4 = Mahasiswa("Rizky Pratama", "2225", "Teknik Mesin", "6", "3.75")
mhs5 = Mahasiswa("Dewi Lestari", "2226", "Teknik Sipil", "7", "3.88")
mhs1.tampilkan_info()
mhs2.tampilkan_info()
mhs3.tampilkan_info()
mhs4.tampilkan_info()
mhs5.tampilkan_info()

