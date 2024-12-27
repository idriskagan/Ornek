#Narsisistik Sayı (veya Armstrong Sayısı), her biri belirli bir tabandaki basamak sayısının kuvvetine yükseltilmiş kendi basamaklarının toplamı olan pozitif bir sayıdır. Bu soruda kendimizi ondalık (taban 10) ile sınırlayacağız.
#Örneğin, narsisistik olan 153'ü (3 basamak) ele alalım: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#ve narsisistik olmayan 1652'yi (4 basamak): 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
#Verilen sayının 10 tabanında Narsisistik bir sayı olup olmadığına bağlı olarak kodunuz doğru veya yanlış ('doğru' ve 'yanlış' ) döndürmelidir.def narsisistik_mi(sayi):
    # Sayıyı string'e dönüştürerek basamak sayısını buluyoruz
    basamaklar = str(sayi)
    basamak_sayisi = len(basamaklar)

    # Basamakların kuvvetlerinin toplamını hesaplıyoruz
    toplam = 0
    for basamak in basamaklar:
        toplam += int(basamak) ** basamak_sayisi

    # Eğer toplam, verilen sayıya eşitse "doğru" döndürüyoruz, değilse "yanlış"
    if toplam == sayi:
        return "doğru"
    else:
        return "yanlış"


# Test
print(narsisistik_mi(153))  # doğru
print(narsisistik_mi(1652))  # yanlış
