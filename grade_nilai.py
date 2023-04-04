while True:
    name_siswa = input("Masukkan Nama anda : ")
    nilai_harian = int(input("Masukkan nilai harian : "))
    nilai_uts = int(input("Masukkan nilai UTS : "))
    nilai_uas = int(input("Masukkan nilai UAS : "))
    nilai_akhir = int(nilai_harian*40/100)+(nilai_uts*30/100)+(nilai_uas*30/100)
    if nilai_akhir >= 85:
        predikat_nilai = 'Amat Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("PredikatAnda = ", predikat_nilai)

    elif nilai_akhir >= 75:
        predikat_nilai = 'Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("PredikatAnda = ", predikat_nilai)

    elif nilai_akhir >= 65:
        predikat_nilai = 'Cukup'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("PredikatAnda = ", predikat_nilai)

    elif nilai_akhir >= 55:
        predikat_nilai = 'Kurang'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("PredikatAnda = ", predikat_nilai)

    else:
        predikat_nilai = 'Kurang Sekali'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("PredikatAnda = ", predikat_nilai)