'''
Bir merminin, yerden belirli bir ilk hız (v0) ve açı (theta) ile fırlatıldığını düşünelim. Hava sürtünmesini ihmal ederek, merminin yörüngesini adım adım simüle eden bir program yaz.
İstenenler:
1. Program, mermi yerden yukarıda olduğu sürece (y >= 0) çalışmaya devam etmeli. Bunu bir while döngüsü ile yapabilirsin.
2. Her bir küçük zaman adımında (dt, örneğin 0.01 saniye), merminin yeni x ve y konumlarını hesapla.
○ vx = v0 * cos(theta) (yatay hız sabittir)
○ vy = v0 * sin(theta) - g * t (dikey hız zamanla değişir)
○ x=vx*t
○ y=(v0*sin(theta)*t)-(0.5*g*t**2)
3. Program, aşağıdaki değerleri bulup ekrana yazdırmalı:
○ Uçuş Süresi: Merminin tekrar yere düştüğü anki toplam zaman.
○ Maksimum Yükseklik: Yörünge boyunca ulaştığı en yüksek y değeri.
○ Menzil: Yere düştüğünde katettiği toplam yatay mesafe (x değeri).
Problem 2: Zıplayan Top
Belirli bir yükseklikten (h0) serbest bırakılan bir topun zıplama hareketini simüle et. Top, her zıpladığında enerjisinin bir kısmını kaybeder ve bir önceki zıplamasındaki yüksekliğin belirli bir oranı (katsayi, örn: 0.7) kadar yükselebilir.
İstenenler:
1. Kullanıcıdan başlangıç yüksekliğini (h0) ve enerji kayıp katsayısını (katsayi) al.
2. Toplamda 5 zıplama için bir for döngüsü kur.
3. Her zıplama için ulaşılan maksimum yüksekliği hesapla ve ekrana yazdır.
4. Eğer bir zıplamada ulaşılan yükseklik 1 santimetreden (0.01 metre) daha az ise,
döngüyü erken sonlandır ve "Top durdu." mesajı ver. (break komutunu araştırabilirsin).
Örnek Çıktı:
İpucu: Zamanı (t) her döngüde dt kadar artır. Maksimum yüksekliği bulmak için, her adımda hesapladığın y değerini o ana kadarki maksimum y değeri ile karşılaştır. Açıları radyana çevirmeyi unutma: radyan = derece * (pi / 180). pi sayısını 3.14159 olarak alabilirsin.

'''

import math

#Veriler
v_0= float(input("Başlangıç hızı:"))
θ= float(input("Atış açısı:"))
g= 9.81
dt= 0.01 

#radyan dönüşümü
θ_radyan= θ*(math.pi/180)

#hız
v_x= v_0*math.cos(θ_radyan)
v_y0= v_0*math.sin(θ_radyan)

#Başlangıç değerleri
t=0
x=0
y=0
max_y=0

#While döngüsü
while y>=0:
    x= v_x*t
    v_y= v_y0-g*t
    y= v_y0*t-0.5*g*t**2
    
    if y>max_y:
        max_y=y
        
    t+= dt
    

#Sonuç
print(f"Uçuş süresi: {t:.2f}saniye")
print(f"Maksimum yükseklik: {max_y:.2f} metre")
print(f"Menzil(x): {x:.2f} metre")
