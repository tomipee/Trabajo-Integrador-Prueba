def contadorVM(cantV, cantM, row, rowPondera):
    if(row == '1'):
        cantV += int(rowPondera)
    else:
        cantM += int(rowPondera)
    return cantV, cantM

def contadorS(cantS, mayor, nivel, finalizo, rowPondera):
    if(mayor >= '18'):
        if(nivel >= '4' and finalizo == '1'):
            cantS += int(rowPondera)
    return cantS

def contadorViviendas(cantViviendas, propietarioVyT, rowPondera, esPropietario):
    cantViviendas += int(rowPondera)
    if(esPropietario == '1'):
        propietarioVyT += int(rowPondera)
    return cantViviendas, propietarioVyT

def maximoMinimo(idMax, idMin, aglomerado):
    max = 0
    min = 99999999999999
    for i in aglomerado:
        if(aglomerado[i] > max):
            max = aglomerado[i]
            idMax = i
        if(aglomerado[i] < min):
            min = aglomerado[i]
            idMin = i   
    return idMax, idMin
        
        