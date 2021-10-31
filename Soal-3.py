#Nama: Raihan Herwin Utama
nilaiTeori = input("Silahkan masukan nilai teori yang anda punya:")
nilaiPraktek = input("Silahkan masukan nilai Praktek yang anda punya:")
nilaiTeori = float(nilaiTeori)
nilaiPraktek = float(nilaiPraktek)
if nilaiTeori >= 70:
    if nilaiPraktek >=70:
        print("Selamat, anda lulus!")
    else:
        print("Anda harus mengulang ujian praktek")
elif nilaiPraktek >= 70:
    if nilaiTeori < 70:
        print("Anda Harus mengulang ujian teori")
elif nilaiTeori < 70:
    if nilaiPraktek < 70:
        print("Anda harus mengulang ujian teori dan praktek")








