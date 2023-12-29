class SeniDanBudaya:
    def __init__(self, nama, jenis):
        self._nama = nama  # Akses modifier protected
        self._jenis = jenis

    def get_nama(self):
        return self._nama

    def get_jenis(self):
        return self._jenis

    def deskripsi(self):
        print(f"Sebuah karya seni dan budaya {self._jenis} dengan nama '{self._nama}'.")

class Lukisan(SeniDanBudaya):
    def __init__(self, nama, teknik, gaya):
        super().__init__(nama, "Lukisan")
        self.__teknik = teknik  # Akses modifier private
        self.gaya = gaya

    def get_teknik(self):
        return self.__teknik

    def deskripsi_lukisan(self):
        print(f"Lukisan '{self._nama}' menggunakan teknik {self.__teknik} dengan gaya {self.gaya}.")

class Tarian(SeniDanBudaya):
    def __init__(self, nama, gerakan, asal):
        super().__init__(nama, "Tarian")
        self.gerakan = gerakan
        self.__asal = asal  # Akses modifier private

    def get_asal(self):
        return self.__asal

    def deskripsi_tarian(self):
        print(f"Tarian '{self._nama}' berasal dari {self.__asal} dengan gerakan khas {self.gerakan}.")

# Contoh penggunaan program
if __name__ == "__main__":
    lukisan1 = Lukisan("Mona Lisa", "Minyak", "Realisme")
    tarian1 = Tarian("Pendet", "Gerakan Tradisional Bali", "Bali")

    # Memanggil method dari class Induk
    print("Nama Lukisan:", lukisan1.get_nama())
    print("Jenis Lukisan:", lukisan1.get_jenis())
    lukisan1.deskripsi()

    print("\nNama Tarian:", tarian1.get_nama())
    print("Jenis Tarian:", tarian1.get_jenis())
    tarian1.deskripsi()

    # Memanggil method dari class Anak
    print("\nTeknik Lukisan:", lukisan1.get_teknik())
    lukisan1.deskripsi_lukisan()

    print("\nAsal Tarian:", tarian1.get_asal())
    tarian1.deskripsi_tarian()