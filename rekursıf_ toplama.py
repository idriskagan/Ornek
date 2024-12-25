#Girilen sayının altındaki 3 veya 5'in tüm katlarının toplamını döndürecek şekilde program yazmanız isteniyor.
#Ek olarak, sayı negatifse, 0 döndürün.
#Not: Sayı hem 3'ün hem de 5'in katıysa, yalnızca bir kez sayın.
#Örnek: 10'un altındaki 3 veya 5'in katları olan tüm doğal sayıları listelersek, 3, 5, 6 ve 9'u elde ederiz. Bu katların toplamı 23'tür.

def katlar(sayi):
    if sayi < 0:
        return 0
    toplam = 0
    for i in range(sayi):
        if i % 3 == 0 or i % 5 == 0:  # 3 veya 5'in katıysa
            toplam += i

    return toplam

sayi = 10
print(katlar(sayi))
