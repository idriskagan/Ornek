#İki sayıyı toplayan ve toplamlarını ikili sayı sisteminde olarak döndüren bir fonksiyon uygulayın. Dönüştürme, toplamadan önce veya sonra yapılabilir.
#Döndürülen ikili sayı bir dize olmalıdır.
#Örnekler: (giriş1, giriş2 --> Çıkış (açıklama)))
#1, 1 --> "10" (1 + 1 = ondalık tabanda 2 veya ikili tabanda 10)
#5, 9 --> "1110" (5 + 9 = ondalık tabanda 14 veya ikili tabanda 1110)

def toplama ( a , b):
    x = int(a+b)
    dizi = []
    while(x >0) :
        if (x<2):
            dizi.append(1)
            x=0
        else:
            dizi.append(int(x%2))
            x=int(x/2)
    dizi.reverse()
    return dizi


print(toplama(4,12))