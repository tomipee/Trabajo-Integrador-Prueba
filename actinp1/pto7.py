import string

numeros = list(map(int, input("Ingrese una lista de numeros separada por espacio: ").split()))

numeros = "-".join(str(num) for num in numeros if num % 3 == 0)

print (numeros)
