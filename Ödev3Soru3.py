'''

Soru 1: Birleştirme Sıralaması (Merge Sort)
Bir tam sayı dizisini birleştirme sıralaması (merge sort) kullanarak sıralayınız. 
Algoritmanızın çalışmasını adım adım gösteriniz ve zaman karmaşıklığını açıklayınız. 
Ayrıca, bu algoritmanın "böl ve yönet" (divide and conquer) stratejisini nasıl kullandığını açıklayınız.

'''
dizi= [16, 24, 7, 11, 67, 3, 36]

def merge_sort(dizi):
    if len(dizi)>1:
        orta= len(dizi)//2
        sol= dizi[:orta]
        sag= dizi[orta:]
        
    
        merge_sort(sol)
        merge_sort(sag)
    
        i= 0
        j= 0
        k= 0

        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j] :
                dizi[k]= sol[i]
                i+=1
        
            else:
                dizi[k]=sag[j]
                j+= 1
            k+= 1
        
        while i < len(sol):
            dizi[k]= sol[i]
            i+= 1
            k+= 1
        
        while j < len(sag):
            dizi[k]= sag[j]
            j+= 1
            k+= 1
        
print('Başlangıç dizisi:', dizi)
merge_sort(dizi)
print('Sıralı dizi:', dizi)


