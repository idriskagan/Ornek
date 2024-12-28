#Genellikle bir şey satın aldığınızda, kredi kartı numaranızın, telefon numaranızın veya en gizli sorunuza verdiğiniz cevabın hala doğru olup olmadığı sorulur.
# Ancak, biri omzunuzun üzerinden bakabileceği için, bunu ekranınızda göstermek istemezsiniz. Bunun yerine, bunu maskeleriz.
#Göreviniz, son dört karakter hariç hepsini '#' olarak değiştiren bir fonksiyon yazmaktır.
#2763547124245#########4245
def maskeleme(numara):

    # Son dört karakteri al
    son4=numara[-4:]
    
    maske_numara= '#' * (len(numara) - 4) + son4
    return maske_numara

numara= "2763547124245"
print(maskeleme(numara))
