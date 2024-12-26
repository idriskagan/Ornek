#Herhangi bir negatif olmayan tam sayıyı argüman olarak alabilen bir fonksiyon oluşturmak ve onu rakamları azalan sırayla döndürmektir. Temelde, rakamları yeniden düzenleyerek mümkün olan en yüksek sayıyı oluşturun.
#Örnek
#Giriş: 42145 Çıkış: 54421
#Giriş: 145263 Çıkış: 654321
#Giriş: 123456789 Çıkış: 987654321
def secerek_sirala(sayı):
    dizi = []
    while sayı > 0:
        dizi.append(sayı % 10)
        sayı = sayı // 10
    for i in range(len(dizi)):
        enk = dizi[i]
        enk_indis = i
        for j in range(i + 1, len(dizi)):
            if dizi[j] < enk:
                enk = dizi[j]
                enk_indis = j

        değiştir = dizi[i]
        dizi[i] = dizi[enk_indis]
        dizi[enk_indis] = değiştir
    yenidizi=dizi[::-1]
    sıralanan = int("".join(map(str, yenidizi)))
    print(sıralanan)


a = 5487
secerek_sirala(a)
