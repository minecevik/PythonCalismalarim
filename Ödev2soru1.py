

filmler = [
    {"ad": "Pulp Fiction", "yil": 1994, "puan": 8.9, "tur": ["Dram", "Suç"]},
    {"ad": "Inception", "yil": 2010, "puan": 8.8, "tur": ["Bilim Kurgu", "Aksiyon"]},
    {"ad": "The Matrix", "yil": 1999, "puan": 8.7, "tur": ["Bilim Kurgu", "Aksiyon"]},
    {"ad": "Parasite", "yil": 2019, "puan": 8.6, "tur": ["Dram", "Gerilim"]},
    {"ad": "Fight Club", "yil": 1999, "puan": 8.8, "tur": ["Dram", "Gerilim"]}
]

# Gerekli kütüphaneleri içe aktar
import numpy as np
import matplotlib.pyplot as plt

# Film veritabanı (liste içinde sözlükler)
filmler = [
    {"ad": "Pulp Fiction", "yil": 1994, "puan": 8.9, "tur": ["Dram", "Suç"]},
    {"ad": "Inception", "yil": 2010, "puan": 8.8, "tur": ["Bilim Kurgu", "Aksiyon"]},
    {"ad": "The Matrix", "yil": 1999, "puan": 8.7, "tur": ["Bilim Kurgu", "Aksiyon"]},
    {"ad": "Parasite", "yil": 2019, "puan": 8.6, "tur": ["Dram", "Gerilim"]},
    {"ad": "Fight Club", "yil": 1999, "puan": 8.8, "tur": ["Dram", "Gerilim"]}
]

#Belirli türdeki filmleri listeleyen fonksiyon
def tur_filtrele(tur_adi):
    print(f"\n'{tur_adi}' türündeki filmler:")
    bulundu = False
    for film in filmler:
        if tur_adi in film["tur"]:
            print(f"- {film['ad']} ({film['yil']}) - Puan: {film['puan']}")
            bulundu = True
    if not bulundu:
        print("Bu türde film bulunamadı.")

#Belirli yıl aralığında film bulan fonksiyon
def yil_araliginda_filmler(baslangic, bitis):
    print(f"\n{baslangic}-{bitis} yılları arasındaki filmler:")
    bulundu = False
    for film in filmler:
        if baslangic <= film["yil"] <= bitis:
            print(f"- {film['ad']} ({film['yil']}) - Puan: {film['puan']}")
            bulundu = True
    if not bulundu:
        print("Bu yıl aralığında film bulunamadı.")

#Ortalama puanı hesaplayan fonksiyon
def ortalama_puan():
    toplam = sum(film["puan"] for film in filmler)
    ort = toplam / len(filmler)
    print(f"\nFilmlerin ortalama puanı: {round(ort, 2)}")

#NumPy ile standart sapmayı hesaplayan fonksiyon
def standart_sapma():
    puanlar = np.array([film["puan"] for film in filmler])
    sapma = np.std(puanlar)
    print(f"\nFilm puanlarının standart sapması: {round(sapma, 3)}")

#Matplotlib ile grafik çizen fonksiyon
def grafik_ciz():
    yillar = [film["yil"] for film in filmler]
    puanlar = [film["puan"] for film in filmler]

    plt.plot(yillar, puanlar, marker="o", linestyle="--", color="purple")
    plt.title("Yıllara Göre Film Puanları")
    plt.xlabel("Yıl")
    plt.ylabel("Puan")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Menü fonksiyonu
def menu():
    while True:
        print("\n--- Film Analiz Menüsü ---")
        print("1. Tür filtresiyle film listesi")
        print("2. Yıl aralığına göre film listesi")
        print("3. Ortalama puanı hesabı")
        print("4. Standart sapma hesabı ")
        print("5. Yıla göre puan grafiği")
        print("0. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            tur = input("Tür girin (örnek: Dram): ")
            tur_filtrele(tur)
        elif secim == "2":
            try:
                bas = int(input("Başlangıç yılı: "))
                bit = int(input("Bitiş yılı: "))
                yil_araliginda_filmler(bas, bit)
            except:
                print("Lütfen geçerli yıl girin.")
        elif secim == "3":
            ortalama_puan()
        elif secim == "4":
            standart_sapma()
        elif secim == "5":
            grafik_ciz()
        elif secim == "0":
            print("Program sonlandırıldı.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

menu()
