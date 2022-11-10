# Program mengurutkan data dari yang terkecil ke besar


print("Program mengurutkan data")
print("===========================")

# Inputan dari user
list = [
    int(input("masukkan angka ke 1:")),
    int(input("masukkan angka ke 2:")),
    int(input("masukkan angka ke 3:")),
    int(input("masukkan angka ke 4:")),
    int(input("masukkan angka ke 5:")),
    int(input("masukkan angka ke 6:"))
]


list.sort()

# hasil urutan bilangan
print("Uturan bilangan :", list)
1