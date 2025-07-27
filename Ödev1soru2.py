#Veriler
h_0= float(input("Başlangıç yüksekliği:"))
katsayi= float(input("Enerji kaybı katsayısı:"))
h= h_0

#Zıplama döngüsü
for i in range(1,6):
    print(i, ".zıplama sonrası yükseklik: ", round(h,2),"m")
    
    h=h*katsayi
    
    
    if h<0.01:
        print("Top durdu.")
        break