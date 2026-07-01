#mengurutkan angka
angka=[4, 6, 8, 1, 3, 5, 7, 2, 9]
#angka=[input(int("Masukkan angka... "))]

#Asceding
for i in range(len(angka)-1):
    for j in range(len(angka)-i-1):
        if angka[j] > angka[j+1]:
            print(f"{angka[j]} lebih besar dari {angka[j+1]}, maka ditukar")
            angka[j], angka[j+1] = angka[j+1], angka[j]
            print(f"Urutan sementara: {angka}")
        else:
            print(f"{angka[j]} lebih kecil dari {angka[j+1]}, maka tidak ditukar")
            print(f"Urutan sementara: {angka}")
            continue

print("Angka setelah diurutkan (ascending):", angka)

#Desceding
for i in range(len(angka)-1):
    for j in range(len(angka)-i-1):
        if angka[j] < angka[j+1]:
            print(f"{angka[j]} lebih kecil dari {angka[j+1]}, maka ditukar")
            angka[j], angka[j+1] = angka[j+1], angka[j]
            print(f"Urutan sementara: {angka}")
        else:
            print(f"{angka[j]} lebih besar dari {angka[j+1]}, maka tidak ditukar")
            print(f"Urutan sementara: {angka}")
            continue

print("Angka setelah diurutkan (descending):", angka)