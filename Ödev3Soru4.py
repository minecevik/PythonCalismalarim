'''

Soru 2: Kabarcık Sıralaması (Bubble Sort)
Bir tam sayı dizisini kabarcık sıralaması (bubble sort) kullanarak sıralayınız. 
Algoritmanızı optimize ederek, eğer bir geçişte hiç yer değiştirme işlemi yapılmadıysa algoritmanın erken sonlanmasını sağlayınız. 
Bu optimizasyonun algoritmanın performansını nasıl etkilediğini açıklayınız.

'''

from array import array

def bubble_sort(dizi):
    for n in range(len(dizi)-1, 0, -1):
        degisim= False
        
        for i in range(n):
            if dizi[i]>dizi[i+1]:
                dizi[i], dizi[i+1]=dizi[i+1], dizi[i]
                degisim= True
         #erken sonlanma      
        if not degisim:
            break
        
dizi=array('i', [16, 24, 7, 11, 67, 3, 36])

print('Sırlanmamış dizi:', dizi.tolist())
bubble_sort(dizi)
print('Sıralanmış dizi:', dizi.tolist())
