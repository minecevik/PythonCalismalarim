'''

Sru 1: İkili Arama (Binary Search)
Artan sırada sıralanmış bir tam sayı dizisinde, verilen bir sayının var olup olmadığını kontrol eden bir ikili arama algoritması uygulayınız. 
Algoritmanızın zaman karmaşıklığını belirtiniz ve neden ikili aramanın doğrusal aramadan daha verimli olduğunu açıklayınız.

'''

import array
sayilar=array.array('i', [2,4,6,8,10,12])

def binary_search(dizi, hedef):
    baslangic= 0
    bitis= len(dizi)-1
    
    while baslangic<=bitis:
        orta= (baslangic+bitis)//2
        
        if dizi[orta]==hedef:
            return orta
        
        elif dizi[orta]<hedef:
            baslangic= orta+1
            
        else:
            bitis=orta-1
            
    return-1
    
hedef=5
sonuc= binary_search(sayilar, hedef)

if sonuc!=-1:
    print(f'{hedef} sayisi {sonuc}. indekste bulundu.')
else:
    print(f'{hedef} sayisi dizide yok. ')

#Zaman karmaşıklığı: O(log2 n)= log2 (6)=3
