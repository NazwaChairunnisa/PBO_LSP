#kelas Kucing sebgai "definisi"
class kucing:
    warna = None
    usia = None

# membangun instansiasi/variable sebagai objek
kucing1 = kucing()
kucing.warna = "hitam"
kucing.usia = "2 Bulan"

# kita panggil kucing 1
print(kucing1.warna, kucing1.usia)