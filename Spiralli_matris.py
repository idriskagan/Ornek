#kendisine parametre olarak gelen n  ile n*n lik spiral matrisi yazınız 
#Örnek :
#1 2 3
#8 9 4
#7 6 5

def spiralli_matris(n):
    # n x n boyutlarında boş bir matris oluşturuyoruz
    matris = [[0] * n for _ in range(n)]

    # Spiralde kullanılacak ilk değer 1
    deger = 1

    # Spiral yönleri: sağ, aşağı, sol, yukarı
    yonler = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    satir, sutun = 0, 0  # Başlangıç noktası
    yon_index = 0  # Başlangıç yönü: sağ

    # Spiral değeri n x n'lik matrisi doldurana kadar devam et
    while deger <= n * n:
        matris[satir][sutun] = deger  # Şu anki pozisyonu doldur
        deger += 1  # Bir sonraki değere geç

        # Bir sonraki hücreyi hesapla
        yeni_satir = satir + yonler[yon_index][0]
        yeni_sutun = sutun + yonler[yon_index][1]

        # Eğer yeni pozisyon geçerli değilse, yönü değiştir
        if 0 <= yeni_satir < n and 0 <= yeni_sutun < n and matris[yeni_satir][yeni_sutun] == 0:
            satir, sutun = yeni_satir, yeni_sutun
        else:
            # Yönü değiştir (saat yönünde)
            yon_index = (yon_index + 1) % 4
            satir += yonler[yon_index][0]
            sutun += yonler[yon_index][1]

    # Sonuç matrisini yazdır
    for satir in matris:
        print(" ".join(map(str, satir)))


# Kullanıcıdan n değerini al
a = int(input("Bir n değeri girin: "))
spiralli_matris(a)
