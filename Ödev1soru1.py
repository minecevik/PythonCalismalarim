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
