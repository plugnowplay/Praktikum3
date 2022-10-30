#input nilai variabel
a = input("masukan nilai pertama: ")
b = input("masukan nilai kedua: ")

#cetak nilai variabel
print("variabel a = ", a)
print("variabel b = ", b)
print("Hasil Penggabungan {1} & {0} = %s".format(a,b) %(a+b))

#konversi nilai variabel 
a = int(a)
b = int(b)


print("Hasil penjumlahan {1} + {0} = %d".format(a,b) %(a+b))
print("Hasil pembagian {1} / {0} = %d".format(a,b) %(a/b))
