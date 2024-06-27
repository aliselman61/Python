import random

def tahmin_oyunu():
    print(" sayı tahmin oyununa hoş geldin. ;)")
    print("1 ile 100 arasında bir sayı tuttum. Bu sayıyı tahmin edebilirmisin?")

    # Bilgisayarın rastgele bir sayı tutması
    sayı = random.randint(1, 100)
    tahminsayısı=(0)
    tahmin_edildi = False

    while not tahmin_edildi:
        try:
            tahmin=int(input("Tahmininizi giriniz (1 ile 100 arası bir sayı): "))
            tahmin_sayisi=(1)

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            if tahmin < sayı:
                print("Daha yüksek bir sayı tahmin edin.")
            elif tahmin > sayı:
                print("Daha düşük bir sayı tahmin edin.")
            else:
                print(f"Tebrikler! {sayı} sayısını {tahmin_sayisi} tahminde buldunuz.")
                tahmin_edildi = True

        except ValueError:
            print("Geçersiz bir değer girdiniz. Lütfen bir tam sayı girin.")
        
    print("Oyunu bitirdiniz. Tekrar oynamak ister misiniz?")

    # Tekrar oynamak isteyip istemediğini sor
    cevap = input("Evet için 'e' Hayır için 'h' yazın: ").strip().lower()
    if cevap == 'e':
        tahmin_oyunu()
    else:
        print("Oyun Bitti Kanka")
        
     #Oyunu Başlat
tahmin_oyunu()
