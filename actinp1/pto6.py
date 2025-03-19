num = [1,2,3,4,5,6,7,8,9,10]

pares = []
impares = []

for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print ("Pares: ", pares)
print ("Impares: ", impares)

