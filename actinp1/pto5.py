numeros = list(map(int, input("Ingrese una lista de numeros separada por espacio: ").split()))

for i in numeros:
    if i < 0:
        break
    print(i)
