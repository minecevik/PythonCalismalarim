'''
Soru 3: E-Ticaret Sipariş Analizi
Bir e-ticaret sitesinin sipariş verilerini analiz eden bir uygulama geliştirmeniz isteniyor.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
# Örnek veri oluşturma (gerçek uygulamada CSV'den yüklenebilir) np.random.seed(42)
urun_kategorileri = ["Elektronik", "Giyim", "Kitap", "Kozmetik", "Ev Eşyası"]
musteri_sehirleri = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Adana"]
siparis_sayisi = 1000
siparisler = {
"siparis_id": range(1, siparis_sayisi + 1),
"tarih": [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _
in range(siparis_sayisi)],
"musteri_id": np.random.randint(1, 201, siparis_sayisi), "urun_id": np.random.randint(1, 51, siparis_sayisi),
"kategori": np.random.choice(urun_kategorileri, siparis_sayisi), "fiyat": np.random.uniform(10, 1000, siparis_sayisi),
"adet": np.random.randint(1, 6, siparis_sayisi),
"sehir": np.random.choice(musteri_sehirleri, siparis_sayisi)
}
# DataFrame oluştur
df_siparisler = pd.DataFrame(siparisler)
# Toplam tutarı hesapla
df_siparisler["toplam_tutar"] = df_siparisler["fiyat"] * df_siparisler["adet"] Bu veri seti üzerinde aşağıdaki işlemleri gerçekleştiren fonksiyonları yazın:
1. Kategori bazında toplam satış tutarını ve adetini hesaplayan bir fonksiyon
2. Şehir bazında ortalama sipariş tutarını hesaplayan bir fonksiyon
3. Belirli bir tarih aralığındaki siparişleri analiz eden bir fonksiyon
4. En çok satılan 5 ürünü bulan bir fonksiyon
5. Aylık satış trendini gösteren ve matplotlib kullanarak görselleştiren bir fonksiyon
6. Kategori bazında satışları pasta grafik olarak gösteren bir fonksiyon
7. Bir kategorideki ürünlerin fiyat dağılımını histogram olarak gösteren bir fonksiyon
 Bu fonksiyonları kullanarak, kullanıcıya hangi analizi görmek istediğini soran ve sonuçları hem sayısal hem de görsel olarak sunan kapsamlı bir rapor sistemi oluşturun
 '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

np.random.seed(42)

# Ürün kategorileri ve şehirler
urun_kategorileri = ["Elektronik", "Giyim", "Kitap", "Kozmetik", "Ev Eşyası"]
musteri_sehirleri = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Adana"]

siparis_sayisi = 1000

siparisler = {
    "siparis_id": range(1, siparis_sayisi + 1),
    "tarih": [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _ in range(siparis_sayisi)],
    "musteri_id": np.random.randint(1, 201, siparis_sayisi),
    "urun_id": np.random.randint(1, 51, siparis_sayisi),
    "kategori": np.random.choice(urun_kategorileri, siparis_sayisi),
    "fiyat": np.random.uniform(10, 1000, siparis_sayisi),
    "adet": np.random.randint(1, 6, siparis_sayisi),
    "sehir": np.random.choice(musteri_sehirleri, siparis_sayisi)
}

df = pd.DataFrame(siparisler)

df["toplam_tutar"] = df["fiyat"] * df["adet"]

#Kategori bazında satış tutarı ve adet
kategori_ozet = df.groupby("kategori")[["toplam_tutar", "adet"]].sum()
print("Kategori Bazında Satış Özeti:\n", kategori_ozet)

#Şehir bazında ortalama sipariş tutar
sehir_ortalama = df.groupby("sehir")["toplam_tutar"].mean()
print("\nŞehir Bazında Ortalama Sipariş Tutarı:\n", sehir_ortalama)

#Belirli bir tarih aralığındaki siparişler
baslangic = "2023-02-01"
bitis = "2023-03-31"
tarih_araligi = df[(df["tarih"] >= baslangic) & (df["tarih"] <= bitis)]
print(f"\n{baslangic} - {bitis} Arası Sipariş Sayısı:", len(tarih_araligi))

#En çok satılan 5 ürün
en_cok_satan = df.groupby("urun_id")["adet"].sum().sort_values(ascending=False).head(5)
print("\nEn Çok Satılan 5 Ürün:\n", en_cok_satan)

#Aylık satış trendi
df["ay"] = df["tarih"].dt.to_period("M")
aylik_trend = df.groupby("ay")["toplam_tutar"].sum()
aylik_trend.plot(kind="line", marker="o", title="Aylık Satış Trendleri")
plt.ylabel("Toplam Satış (₺)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Kategori bazında pasta grafik
kategori_ozet["toplam_tutar"].plot(kind="pie", autopct="%.1f%%", title="Kategori Bazında Satış Dağılımı", ylabel="")
plt.tight_layout()
plt.show()

#Kategori bazında fiyat dağılımı
plt.figure(figsize=(10,6))
for kategori in urun_kategorileri:
    plt.hist(df[df["kategori"] == kategori]["fiyat"], alpha=0.6, bins=20, label=kategori)

plt.title("Kategoriye Göre Fiyat Dağılımı")
plt.xlabel("Fiyat (₺)")
plt.ylabel("Ürün Sayısı")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
