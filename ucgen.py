#a, b, c olmak üzere 3 tamsayı değerini kabul eden bir fonksiyon uygulayın. Belirtilen uzunluktaki kenarlarla bir üçgen oluşturulabiliyorsa fonksiyon true değerini döndürmelidir;
#diğer durumlarda false değerini döndürmelidir.(Bu durumda tüm üçgenlerin kabul edilebilmesi için yüzeylerinin 0'dan büyük olması gerekir).

def ucgen(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


print(ucgen(3, 4, 5))
print(ucgen(1, 2, 3))
print(ucgen(5, 5, 0))
