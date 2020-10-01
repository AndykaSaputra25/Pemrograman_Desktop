def m3(nilai):
    nilai.sort()
    print("Nilai: ", nilai)
#___MEAN___#
    mean = sum(nilai) / len(nilai)
    print("\nRata-Rata (mean): ", mean)
#___MEDIAN___#
    tot=0
    x = len(nilai) // 2
    if len(nilai) % 2 == 1:
        print("Nilai Tengah (median): ", nilai[x])
    else: 
        tot = (nilai[x] + nilai[x-1]) / 2
        print("Nilai Tengah (median): ", tot)
#___MODUS___#
    tampung=[]
    i=0
    while i < len(nilai) : 
        tampung.append(nilai.count(nilai[i])) 
        i += 1
    d1 = dict(zip(nilai, tampung)) 
    d2 = {k for (k,v) in d1.items() if v == max(tampung) }
    print("Nilai sering muncul (modus): " + str(d2))
nilai = [13, 34, 26, 26, 21]
m3(nilai)