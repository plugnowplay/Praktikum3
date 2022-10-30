# Tugas Pertemuan 6 Praktikum 3 <hr> <br>

## Daftar isi 
1. [Latihan 1](#Latihan-1)
2. [Latihan 2](#Latihan-2)
3. [Latihan 3](#Latihan-3)
4. [Menghitung luas dan keliling lingkarn menggunakan `Python`](#Menghitung-luas-dan-keliling-lingkarn-menggunakan-`Python`)

# Latihan 1
<br>
* buat Source Code <br>

![SC latihan1](https://user-images.githubusercontent.com/47426095/198815060-adb529f3-1b8f-478c-aa5c-84292c55e64c.png)
```python 
#penggunaan end
print('A', end=' ')
print('B', end=' ')
print('C', end=' ')
print()
print('X')
print('Y')
print('Z')

# penggunaan separator
w,x,y,z = 10,15,20,25
print(w,x,y,z)
print(w,x,y,z, sep = ',')
print(w,x,y,z, sep = '')
print(w,x,y,z, sep = ':')
print(w,x,y,z, sep = '-----')

#string format
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format
print('{0:3} {1:>16}'.format(0, 10**0))
print('{0:3} {1:>16}'.format(1, 10**1))
print('{0:3} {1:>16}'.format(2, 10**2))
print('{0:3} {1:>16}'.format(3, 10**3))
print('{0:3} {1:>16}'.format(4, 10**4))
print('{0:3} {1:>16}'.format(5, 10**5))
print('{0:3} {1:>16}'.format(6, 10**6))
print('{0:3} {1:>16}'.format(7, 10**7))
print('{0:3} {1:>16}'.format(8, 10**8))
print('{0:3} {1:>16}'.format(9, 10**9))
print('{0:3} {1:>16}'.format(10, 10**10))
```

* Lakukan Run File
* Hasil Output : <br>
![run latihan1](https://user-images.githubusercontent.com/47426095/198815125-3cfb5640-7129-460c-a8a2-99435eb5272a.PNG)
<br>

```

A B C 
X
Y
Z
10 15 20 25
10,15,20,25
10152025
10:15:20:25
10-----15-----20-----25
0 1
1 10
2 100
3 1000
4 10000
5 100000
6 1000000
7 10000000
8 100000000
9 1000000000
10 10000000000
  0                1
  1               10
  2              100
  3             1000
  4            10000
  5           100000
  6          1000000
  7         10000000
  8        100000000
  9       1000000000
 10      10000000000

```
<br><br>

# Latihan 2 

* buat kode <br>
![SC latihan2](https://user-images.githubusercontent.com/47426095/198815274-cb1ce429-aad3-4646-979f-e659fc7c3af3.PNG)
<br>

```python
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
```

* lakukan run file
* hasil output :
![run latihan2](https://user-images.githubusercontent.com/47426095/198815344-e7835741-519d-4562-bdbc-7ffa4ac92592.PNG)
<br>

```
masukan nilai pertama: 2
masukan nilai kedua: 5
variabel a =  2
variabel b =  5
Hasil Penggabungan 5 & 2 = 25
Hasil penjumlahan 5 + 2 = 7
Hasil pembagian 5 / 2 = 0
```
# Latihan 3
* buat kode <br>
![SC latihan3](https://user-images.githubusercontent.com/47426095/198815446-deadbac8-b4c3-46c4-8073-bdcf003872e8.PNG)
<br>

```python
h = 5
print("Hello ini script python \n\n")

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
```

* lakukan run file
* Hasil Output : <br>
![run latihan3](https://user-images.githubusercontent.com/47426095/198815514-f20acf7e-5e0b-4fcd-a399-d1b6c138a021.PNG)
<br>

```
Hello ini script python 


      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *
```
* Flowchart : <br>
![Map latihan3](https://user-images.githubusercontent.com/47426095/198815566-ce5e09e8-ca92-4121-9111-23b7637f9715.png)


# Menghitung luas dan keliling lingkarn menggunakan `Python`

1. Buat File bernama luasKelilingLingkaran.py
2. Berikut Flowchart untuk menghitung luas dan keliling lingkaran

   <img width="625" alt="flow" src="https://user-images.githubusercontent.com/115965039/198862746-0294dbd5-2951-4216-9344-0d8fbb49ef95.png">


4. Lalu Masukan CODE berikut :

    ```python
      # import module math
    import math

    # Variable jariJari menampung nilai input yang dimasukan yaitu berupa string
    jariJari = input('Masukan jari-jari lingkaran :')

    """

    rumus luas & keliling lingkaran
    _____________________________________

    luas     = phi * r^2

    keliling = 2 * phi * r

    _____________________________________

    """

    # convert string to integer
    jariJari = int(jariJari)

    # hitung luas lingkaran
    luas = math.pi * (jariJari * jariJari)

    # hitung luas keliling
    keliling = 2 * math.pi * jariJari

    # output luas & keliling lingkaran
    # .2f => mengambil 2 angka setelah (,)
    print("Berikut Luas lingkaran =  ", format(luas, '.2f'))
    print("Berikut Keliling lingkaran = ", format(keliling, '.2f'))

    ```

4. Ketika dijalankan Inputkan Jari jari dan Berikut Hasil nya

![hasil](https://user-images.githubusercontent.com/115965039/198862801-28bb7c6e-9f54-47a4-9e9f-17921875bd2f.png)



5. Selesai Begitulah cara menghitung luas dan keliling Lingkaran
