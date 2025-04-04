def sumar_estadisticas(ronda_final,ronda_normal,estadistica,stats,jugador):
    if estadistica == 'kills':
        if(stats[estadistica] != 0):
            punto = stats[estadistica] * 3
            ronda_final[jugador]['kills'] += stats[estadistica]
            ronda_final[jugador]['puntos'] += punto
            ronda_normal[jugador][estadistica] += stats[estadistica]
    if estadistica == 'assists':
        if(stats[estadistica] != 0):
            punto = stats[estadistica] * 1
            ronda_final[jugador]['assists'] += stats[estadistica]
            ronda_final[jugador]['puntos'] += punto
            ronda_normal[jugador][estadistica] += stats[estadistica]
    if estadistica == 'deaths':
        if stats[estadistica]:
            ronda_final[jugador][estadistica] += 1
            ronda_final[jugador]['puntos'] -= 1  
            ronda_normal[jugador][estadistica] = True







def dividirLinea(palabra):
    e = palabra.split()
    return e

def lineaTipo(elem, menciones):
    for n in elem:
        if n in menciones:
            menciones[n]+=1

def contarPalabras(cant, palabra):
   for n in palabra:
        cant = cant + 1
   return cant


max = 0
eMax = ""
def calcularMax(cant, e):
    global max
    global eMax
    if cant > max:
        max = cant
        eMax = e
        return [max,eMax]
    return[max,eMax]

def ingreseString (x):
    x = input("Ingrese por teclado...")
    return x

def seEncuentra(x,palabras):
    palabra = palabras.split()
    esta = False
    for elem in palabra:
     if elem == x :
         esta = True
    if(esta):
        print(palabras)
    return(None)

def evaluarCaracter(x,l):
    if x.isdigit():
        l[1] = True
    if x.isupper():
        l[2] = True
    if not x.isalnum():
        l[3] = False
    
def clean_name(name):
    if name in [""," ","  ",None]:
        return None
    else:
        return name.strip().title() if name else None
     
        