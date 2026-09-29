class Pegawai:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    def tampilkan_pegawai(self):
        print("ID Pegawai  :", self.id_pegawai)
        print("Nama        :", self.nama)
        print("Gaji        : Rp", self.gaji)


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def tampilkan_proyek(self):
        print("Nama Proyek :", self.nama_proyek)


class ProjectManager(Pegawai, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_data(self):
        self.tampilkan_pegawai()
        self.tampilkan_proyek()


pm1 = ProjectManager(
    "PM101",
    "Dimas Arya Saputra",
    7500000,
    "Pengembangan Aplikasi Perpustakaan"
)

pm2 = ProjectManager(
    "PM102",
    "Siti Nur Aisyah",
    8800000,
    "Sistem Informasi Rumah Sakit"
)

pm3 = ProjectManager(
    "PM103",
    "Rafi Muhammad Pratama",
    9500000,
    "Platform Pembelajaran Online"
)


print("DATA PROJECT MANAGER 1")
pm1.tampilkan_data()
print()

print("DATA PROJECT MANAGER 2")
pm2.tampilkan_data()
print()

print("DATA PROJECT MANAGER 3")
pm3.tampilkan_data()