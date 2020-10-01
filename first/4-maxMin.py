def maxMin():
    banyak = int(input("Berapa banyak angka: "))
    posisi = []
    first=0
    while first <= banyak-1:
        posisi.append(int(input("Angka ke-{0}: ".format(first))))
        first+=1
    posisi.sort()
    print(posisi)
    
    print("\nMin: ", posisi[0])
    print("Max: ", posisi[-1])
maxMin()