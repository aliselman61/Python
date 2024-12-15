using System;

class SayiTahminOyunu
{
    static void Main()
    {
        Random rastgele = new Random();
        int hedefSayi = rastgele.Next(1, 101); // 1 ile 100 arasında rastgele bir sayı seçiliyor.
        int tahminSayisi = 0;
        bool dogruTahmin = false;

        Console.WriteLine("Sayı Tahmin Oyununa Hoş Geldin");
        Console.WriteLine("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?");

        while (!dogruTahmin)
        {
            Console.Write("Lütfen tahmininizi girin: ");
            string giris = Console.ReadLine();

            if (int.TryParse(giris, out int tahmin))
            {
                tahminSayisi++;

                if (tahmin < hedefSayi)
                {
                    Console.WriteLine("Daha büyük bir sayı deneyin.");
                }
                else if (tahmin > hedefSayi)
                {
                    Console.WriteLine("Daha küçük bir sayı deneyin.");
                }
                else
                {
                    dogruTahmin = true;
                    Console.WriteLine($"Tebrikler! {tahminSayisi} denemede doğru tahmin yaptınız.");
                }
            }
            else
            {
                Console.WriteLine("Geçerli bir sayı giriniz.");
            }
        }

        Console.WriteLine("Oyun bitti. Çıkmak için bir tuşa basın.");
        Console.ReadKey();
    }
}
