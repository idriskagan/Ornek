def maskeleme(numara):
    # Son dört karakteri al
 son4=numara[-4:]
    
 maske_numara= '#' * (len(numara) - 4) + son4
 return maske_numara

numara= "2763547124245"
Numara = maskeleme(numara)
print(numara)