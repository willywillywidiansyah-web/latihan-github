print("Halo Python")

#VARIABEL dan TIPE DATA
#Variabel number
# Tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)

# Tipe data floating numbers
a = 7.5

print(a)

#Variabel string
# Menggunakan single quote
myFirstName = 'Rizqi'

# Menggunakan double quote
myLastName = "Maulana"

# Penulisan Angka sebagai string
myAge = "25"

# Penulisan string multiline
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""

# Mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)

#Variabel boolean
# Contoh penulisan boolean yang benar
a = True
b = False
print(a)

# Contoh penulisan boolean yang salah
# Jika dijalankan, pada baris ini akan error
#c = true
#print(c)

#OPERATOR
# Operator Aritmatika
a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16

#Operator Perbandingan(Comparison)
a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16

#Operator Logika
a = 3
b = 9

# Contoh Penggunaan "and"
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# Contoh Penggunaan "or"
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# Contoh Penggunaan "not"
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True

#KONDISI IF ELSE PADA PYTHON
#If
"""
Note:
Penulisan kode di dalam blok atau scope pada Python bergantung pada Indentation (spasi di awal baris). Contoh jika kita ingin 
menulis kode di dalam blok/scope Statemen if, maka penulisanny seperti ini:
"""

# Penulisan yang benar:
if(True):
    print("Benar.") # ada spasi di awal baris (lebih menjorok ke dalam)

# Penulisan yang salah:
#if(True):
#print("Benar.") # tidak ada spasi di awal baris (sejajar dengan kode di atasnya)
#If condition
x = 5
y = 10

# karena x lebih kecil dari y adalah benar. maka kode di dalam scope statemen if akan dijalankan.
if(x < y):
    print("nilai x lebih kecil dari y.") # ini akan dijalankan

# karena x lebih besar dari y adalah salah. maka kode di dalam scope statemen if tidak akan dijalankan.
if(x > y):
    print("nilai x lebih besar dari y.") # ini tidak akan dijalankan

#Elif
#condition if elif
a = 80

# disini kita melakukan pengecekan kedua dan ketiga jika pada statemen if bernilai False. Kode pada blok ini
# akan dijalankan hanya jika statemen elif bernilai True.

# Pengecekan pertama dengan if: if(a > 90)
# Pengecekan kedua dengan elif: elif(a > 70)

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini akan dijalankan 

#Else
#Condition if else
a = 60

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini tidak akan dijalankan
else:
    print("Dapat nilai C.") # ini akan dijalankan

#PERULANGAN (LOOPING) PADA PYTHON
#For 
# for loop 1
# Mencetak kata "Halo Python" sebanyak 5 kali
for (x) in range(5):
    print("Halo Python.")
# for loop 2
# Mencetak semua item pada variabel fruits (lists)
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf satu per satu pada kata "Indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)
    
#While
# loop while
# Mencetak angka, jika angka lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1

#Break dan Continue
#loop for break
# Menghentikan perulangan jika nilai x adalah 3
# Pada kode di bawah ini, jika nilai x sama dengan 3,
# maka perulangan akan dihentikan. Walaupun seharusnya
# perulangan akan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 3:
        break
#loop for continue
# Melewati perulangan jika nilai x adalah angka genap (2, 4, 6 dst)
# Pada kode di bawah ini, hanya akan mencetak angka ganjil 
# karena jika angka adalah genap,maka proses mencetak akan
# kita skip menggunakan keyword "continue"

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
