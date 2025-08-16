'''
Problem 3: Asal Sayılar
Matematik ve kriptografi gibi alanlarda temel olan asal sayıları bulan bir program yaz.
İstenenler:
1. Program, 2'den 100'e kadar olan bütün sayıları kontrol etmeli (dış for döngüsü).
2. Her bir sayının asal olup olmadığını kontrol etmek için, o sayıyı 2'den başlayıp kendisine kadar
olan sayılara bölmeye çalış (iç for döngüsü).
3. Eğer bir sayı, kendisinden küçük (ve 1'den büyük) hiçbir sayıya tam bölünmüyorsa, o sayı asaldır.
4. Bulduğun tüm asal sayıları ekrana yazdır.
5. Ekstra Zorluk: Asal sayıları bulduktan sonra, aralarındaki fark 2 olan "ikiz asalları" (örn: (3, 5), (5,
7), (11, 13)) bulup onları da ayrıca listele.
'''

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
