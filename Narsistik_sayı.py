def narsisistik_mi(sayi):
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
