'''
Problem 2: Zıplayan Top
Belirli bir yükseklikten (h0) serbest bırakılan bir topun zıplama hareketini simüle et. Top, her zıpladığında enerjisinin bir kısmını kaybeder ve bir önceki zıplamasındaki yüksekliğin belirli bir oranı (katsayi, örn: 0.7) kadar yükselebilir.
İstenenler:
1. Kullanıcıdan başlangıç yüksekliğini (h0) ve enerji kayıp katsayısını (katsayi) al.
2. Toplamda 5 zıplama için bir for döngüsü kur.
3. Her zıplama için ulaşılan maksimum yüksekliği hesapla ve ekrana yazdır.
4. Eğer bir zıplamada ulaşılan yükseklik 1 santimetreden (0.01 metre) daha az ise,
döngüyü erken sonlandır ve "Top durdu." mesajı ver. (break komutunu araştırabilirsin).
'''

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
