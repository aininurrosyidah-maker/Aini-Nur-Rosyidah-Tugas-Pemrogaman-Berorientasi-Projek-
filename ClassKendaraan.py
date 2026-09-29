class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_data(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jumlah Kursi :", self.jumlah_kursi)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Tipe Motor :", self.tipe_motor)


# 3 Objek Mobil
mobil1 = Mobil("Fortuner", "Toyota", 2024, 195, 7)
mobil2 = Mobil("Pajero Sport", "Mitsubishi", 2023, 190, 7)
mobil3 = Mobil("Brio", "Honda", 2022, 160, 5)


# 3 Objek Motor
motor1 = Motor("Aerox", "Yamaha", 2024, 145, "Matic")
motor2 = Motor("Vario 160", "Honda", 2023, 135, "Matic")
motor3 = Motor("KLX 150", "Kawasaki", 2022, 120, "Trail")


print("DATA MOBIL 1")
mobil1.tampilkan_data()
print()

print("DATA MOBIL 2")
mobil2.tampilkan_data()
print()

print("DATA MOBIL 3")
mobil3.tampilkan_data()
print()

print("DATA MOTOR 1")
motor1.tampilkan_data()
print()

print("DATA MOTOR 2")
motor2.tampilkan_data()
print()

print("DATA MOTOR 3")
motor3.tampilkan_data()
print()