angka1 = int(input('Masukkan Bilangan Ke 1 :'))
angka2 = int(input('Masukkan Bilangan Ke 2 :'))
angka3 = int(input('Masukkan Bilangan Ke 3 :'))
angka4 = int(input('Masukkan Bilangan Ke 4 :'))
angka5 = int(input('Masukkan Bilangan Ke 5 :'))
angka6 = int(input('Masukkan Bilangan Ke 6 :'))
angka7 = int(input('Masukkan Bilangan Ke 7 :'))
angka8 = int(input('Masukkan Bilangan Ke 8 :'))
angka9 = int(input('Masukkan Bilangan Ke 9 :'))
angka10 = int(input('Masukkan Bilangan Ke 10 :'))
angka = [angka1,angka2,angka3,angka4,angka5,angka6,angka7,angka8,angka9,angka10]
angka.sort()
print('Bubble sort Ascending : ', angka)

angka.sort(reverse=True)
print('Bubble sort Descending : ', angka)