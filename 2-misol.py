# 4-misol
def sonlar_(a):
    musbat = []
    manfiy = []
    nol = []
    
    for son in a:
        if son > 0:
            musbat.append(son)
        elif son < 0:
            manfiy.append(son)
        else:
            nol.append(son)
    return musbat, manfiy, nol

royxat = [14,-15,0,2,-6,8,18,0]
musbat, manfiy, nol = sonlar_(royxat)
print(musbat)
print(manfiy)
print(nol)
