import string


def kelimeyi_dönüştür(kelime):
    noktalama = string.punctuation
    noktalama_isareti = ""
    if kelime[-1] in noktalama:
        noktalama_isareti = kelime[-1]
        kelime = kelime[:-1]  # Noktalama işaretini kelimeden çıkar

    dönüştürülmüş = kelime[1:] + kelime[0] + "ay"

    # Eğer kelimenin sonunda noktalama varsa ekle
    return dönüştürülmüş + noktalama_isareti


def cümleyi_dönüştür(cümle):
    # Cümleyi kelimelere ayır
    kelimeler = cümle.split()

    # Dönüştürülmüş kelimeleri tutacak listeyi başlat
    dönüştürülmüş_kelimeler = []

    # Her kelimeyi dönüştür
    for kelime in kelimeler:
        dönüştürülmüş_kelime = kelimeyi_dönüştür(kelime)
        dönüştürülmüş_kelimeler.append(dönüştürülmüş_kelime)

    # Dönüştürülmüş kelimeleri birleştir
    sonuç = " ".join(dönüştürülmüş_kelimeler)

    return sonuç


# Test
cümle = "İlerleyen Dünya!"
sonuç = cümleyi_dönüştür(cümle)
print(sonuç)
