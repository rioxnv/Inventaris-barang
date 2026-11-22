class Barang:

    def __init__(self, kode, nama, stok, harga):
        self.kode = kode
        self.nama = nama
        self.stok = stok
        self.harga = harga

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        if not isinstance(nilai, str) or not nilai.strip():
            raise ValueError("Nama barang tidak boleh kosong.")
        self.__nama = nilai.strip()

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if not isinstance(nilai, int) or nilai < 0:
            raise ValueError("Stok harus berupa bilangan bulat >= 0.")
        self.__stok = nilai

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            raise ValueError("Harga harus berupa angka >= 0.")
        self.__harga = float(nilai)

    def tambah_stok(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("Jumlah penambahan harus bilangan bulat positif.")
        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("Jumlah pengurangan harus bilangan bulat positif.")
        if jumlah > self.stok:
            raise ValueError("Stok tidak mencukupi.")
        self.stok -= jumlah

    def tampilkan_info(self):
        print(
            f"{self.kode:<10} {self.nama:<22} "
            f"{self.stok:<8} Rp{self.harga:,.0f}"
        )

class Inventaris:

    total_barang = 0 

    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_barang = {}

    @staticmethod
    def validasi_kode(kode):
        return isinstance(kode, str) and kode.strip().isalnum() and len(kode) >= 3

    @classmethod
    def jumlah_jenis_barang(cls):
        return cls.total_barang

    def tambah_barang(self, barang):
        if not self.validasi_kode(barang.kode):
            raise ValueError("Kode minimal 3 karakter dan hanya boleh huruf/angka.")
        if barang.kode in self.daftar_barang:
            raise ValueError("Kode barang sudah digunakan.")
        self.daftar_barang[barang.kode] = barang
        Inventaris.total_barang += 1
        print("Barang berhasil ditambahkan.")

    def cari_barang(self, kode):
        return self.daftar_barang.get(kode)

    def tampilkan_semua(self):
        if not self.daftar_barang:
            print("Belum ada data barang.")
            return

        print("\nDAFTAR BARANG")
        print("-" * 65)
        print(f"{'KODE':<10} {'NAMA BARANG':<22} {'STOK':<8} HARGA")
        print("-" * 65)
        for barang in self.daftar_barang.values():
            barang.tampilkan_info()
        print("-" * 65)

    def ringkasan(self):
        total_unit = sum(barang.stok for barang in self.daftar_barang.values())
        nilai_persediaan = sum(
            barang.stok * barang.harga for barang in self.daftar_barang.values()
        )
        print(f"Jumlah jenis barang : {self.jumlah_jenis_barang()}")
        print(f"Total unit stok     : {total_unit}")
        print(f"Nilai persediaan    : Rp{nilai_persediaan:,.0f}")

def input_angka(pesan, tipe=int):
    while True:
        try:
            return tipe(input(pesan))
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

def jalankan_program():
    inventaris = Inventaris("Toko Saya")

    while True:
        print(f"\n=== SISTEM INVENTARIS {inventaris.nama_toko.upper()} ===")
        print("1. Tambah barang")
        print("2. Tampilkan semua barang")
        print("3. Tambah stok")
        print("4. Kurangi stok")
        print("5. Cari barang")
        print("6. Ringkasan inventaris")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                kode = input("Kode barang (min. 3 karakter): ").strip().upper()
                nama = input("Nama barang: ")
                stok = input_angka("Stok awal: ")
                harga = input_angka("Harga satuan: ", float)
                inventaris.tambah_barang(Barang(kode, nama, stok, harga))

            elif pilihan == "2":
                inventaris.tampilkan_semua()

            elif pilihan == "3":
                kode = input("Masukkan kode barang: ").strip().upper()
                barang = inventaris.cari_barang(kode)
                if barang:
                    jumlah = input_angka("Jumlah stok yang ditambahkan: ")
                    barang.tambah_stok(jumlah)
                    print("Stok berhasil ditambahkan.")
                else:
                    print("Barang tidak ditemukan.")

            elif pilihan == "4":
                kode = input("Masukkan kode barang: ").strip().upper()
                barang = inventaris.cari_barang(kode)
                if barang:
                    jumlah = input_angka("Jumlah stok yang dikurangi: ")
                    barang.kurangi_stok(jumlah)
                    print("Stok berhasil dikurangi.")
                else:
                    print("Barang tidak ditemukan.")

            elif pilihan == "5":
                kode = input("Masukkan kode barang: ").strip().upper()
                barang = inventaris.cari_barang(kode)
                if barang:
                    print("\nKODE       NAMA BARANG            STOK     HARGA")
                    barang.tampilkan_info()
                else:
                    print("Barang tidak ditemukan.")

            elif pilihan == "6":
                inventaris.ringkasan()

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan menu tidak tersedia.")

        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")

if __name__ == "__main__":
    jalankan_program()
