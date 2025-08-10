'''

Soru 2: Doğrusal Arama (Linear Search)
Bir dizi içinde tekrar eden elemanları bulunuz.
Doğrusal arama algoritması kullanarak bir dizideki belirli bir sayının tüm konumlarını (indekslerini) döndüren bir fonksiyon yazınız.
Örneğin [4, 2, 7, 4, 8, 4] dizisinde 4 sayısı 0, 3 ve 5 indekslerinde bulunmaktadır.

'''
#Bir dizi içinde tekar eden elemanlar

from array import array

dizi= array('i', [4, 2, 7, 4, 8, 4, 5, 2])

def tekrarlayan_elemanlari_bulma(dizi):
    tekrarlayan_elemanlar= array('i')
    kontrol_edilen_elemanlar= array('i')
    
    for i in range(len(dizi)):
        eleman= dizi[i]
        
        if eleman not in kontrol_edilen_elemanlar:
            sayi_adedi= dizi.tolist().count(eleman)
            
            if sayi_adedi > 1:
                tekrarlayan_elemanlar.append(eleman)
            kontrol_edilen_elemanlar.append(eleman)
    return tekrarlayan_elemanlar

sonuc= tekrarlayan_elemanlari_bulma(dizi)
print('Tekrarlayan elemanlar:', sonuc.tolist())

#Linear Search algoritmasını kullanarak sayısının konumunu döndüren fonksiyon

aranan_sayi= int(input('Hangi sayıyı aramak istiyorsunuz ?:'))

bulundu= False

for i in range(len(dizi)):
    if dizi[i]==aranan_sayi:
        print(f"{aranan_sayi} sayısı {i} konumunda bulundu.")
        bulundu= True
        
if not bulundu:
    print(f"{aranan_sayi} sayısı dizide bulunamadı.")