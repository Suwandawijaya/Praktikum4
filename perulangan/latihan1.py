# perulangan bertingkat (for loop & Nested loop)
# Menentukan seberapa banyak perulangannya yaitu sebanyak 10 kali.
ulang = 10

# variable x & y untuk menampung indeks dan fungsi range() berfungsi untuk membuat list dengan range 0-10
for x in range(ulang):
    for y in range(ulang):
        print(x+y, " ", end=" ")
    print()