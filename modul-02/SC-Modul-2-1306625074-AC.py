# Program Mencari Faktor Bilangan

# Header dan Input Identitas
print ("Program Faktor Bilangan")
print ("Nama \t: Andita Chairunsukma")
print ("NIM \t: 1306625074")

print ()

# Program
while True:

    hasil =[]
    n = int(input('Masukkan Bilangan <100 (Selesai = 0) ='))
    if n == 0:
        break
    for i in range (1, n+1):
        if n % 1 == 0:

            hasil.append(i)
    print('Bilanga', i, 'Faktornya=', hasil)

print('Selesai')
