import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri = {
    'Tarih': pd.date_range(start='2025-01-01', periods=30, freq='D'),
    'Sıcaklık': np.random.randint(5, 30, size=30),
    'Nem': np.random.randint(40, 90, size=30),
    'Yağış': np.random.choice([0, 0.2, 0.5, 1.0, 0], size=30)
}

df = pd.DataFrame(veri)

print("1. Temel İstatistikler:\n")
for sutun in ['Sıcaklık', 'Nem', 'Yağış']:
    print(f"{sutun} - Ortalama: {df[sutun].mean():.2f}, Medyan: {df[sutun].median():.2f}, Min: {df[sutun].min()}, Max: {df[sutun].max()}")

#20°C üstü günler
esik = 20
sicak_esik = df[df['Sıcaklık'] > esik]
print(f"\n2. {esik}°C üstü günler ({len(sicak_esik)} gün):\n", sicak_esik[['Tarih', 'Sıcaklık']])

#Yağışlı günlerdeki nem ortalaması
yagisli_gunler = df[df['Yağış'] > 0]
nem_ort = yagisli_gunler['Nem'].mean()
print(f"\n3. Yağışlı Günlerde Nem Ortalaması: {nem_ort:.2f}")

#Belirli tarih aralığındaki veriler
baslangic = '2025-01-10'
bitis = '2025-01-20'
filtreli = df[(df['Tarih'] >= baslangic) & (df['Tarih'] <= bitis)]
print(f"\n4. {baslangic} - {bitis} tarihleri arası veriler:\n", filtreli)

#Sıcaklık ve nem arasındaki korelasyon
korelasyon = np.corrcoef(df['Sıcaklık'], df['Nem'])[0, 1]
print(f"\n5. Sıcaklık ve Nem Arasındaki Korelasyon: {korelasyon:.2f}")

#Grafik çizimi
plt.figure(figsize=(10, 5))
plt.plot(df['Tarih'], df['Sıcaklık'], label='Sıcaklık (°C)', color='red')
plt.plot(df['Tarih'], df['Nem'], label='Nem (%)', color='blue')
plt.plot(df['Tarih'], df['Yağış'], label='Yağış (mm)', color='green')
plt.xlabel('Tarih')
plt.ylabel('Değer')
plt.title('Hava Durumu Verileri')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
