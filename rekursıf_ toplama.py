def ayırma ( sayı, index):
    if index == len(sayı):
        return 0
    if sayı[index] <0:
        return sayı[index] + ayırma(sayı,index+1)
    else:
        return ayırma(sayı,index+1)
dizi = [1,-2,3,-1,4,0]
print(ayırma(dizi,0))
