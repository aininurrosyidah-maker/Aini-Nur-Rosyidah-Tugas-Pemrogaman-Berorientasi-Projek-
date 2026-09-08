class Buku:
    def __init__(self, judul, penulis, terbit, halaman):
        self.judul = judul
        self.penulis = penulis
        self.terbit = terbit
        self.halaman = halaman

    def info_buku(self):
        print("Judul:", self.judul)
        print("Penulis:", self.penulis)
        print("Tahun terbit:", self.terbit)
        print("Jumlah halaman:", self.halaman)
        print("-----------------------------")  

buku1 = Buku("Janji", "Tere Liye", "2021", "488 halaman")
buku2 = Buku("Samudra", "Nisa Rahmadani", "2022", "396 halaman")
buku3 = Buku("Bumi", "Tere Liye", "2020", "440 halaman")
buku4 = Buku("Hujan", "Tere Liye", "2019", "318 halaman")
buku5 = Buku("Matahari", "Tere Liye", "2018", "390 halaman")
buku1.info_buku()
buku2.info_buku()
buku3.info_buku()
buku4.info_buku()
buku5.info_buku()

