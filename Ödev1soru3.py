#Boş bir liste oluşturuyorum
asal_sayilar= []

for sayi in range(2,101):
    asal=True 
    
    #sayının asal olup olmadığını kontrol etmek için
    for bolen in range(2, sayi):
        if sayi % bolen ==0:
            asal= False
            break
        
    if asal:
        asal_sayilar.append(sayi)
            
print("Asal sayılar:")
print(asal_sayilar)



#İkiz asallar
ikiz_asallar=[]

for sayi in asal_sayilar:
    if(sayi+2) in asal_sayilar:
        ikiz_asallar.append((sayi, sayi+2))
        
print("\nİkiz asal sayılar:")
for ikiz in ikiz_asallar:
    print(ikiz)
