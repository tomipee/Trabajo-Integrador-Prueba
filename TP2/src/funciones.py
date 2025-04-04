def sumar_estadisticas(ronda_final,mvp_porpartida,estadistica,stats,jugador):
    if estadistica == 'kills':
        if(stats[estadistica] != 0):
            punto = stats[estadistica] * 3
            ronda_final[jugador]['kills'] += stats[estadistica]
            ronda_final[jugador]['puntos'] += punto
            mvp_porpartida[jugador] += punto
    if estadistica == 'assists':
        if(stats[estadistica] != 0):
            punto = stats[estadistica] * 1
            ronda_final[jugador]['assists'] += stats[estadistica]
            ronda_final[jugador]['puntos'] += punto
            mvp_porpartida[jugador] += punto
    if estadistica == 'deaths':
        if stats[estadistica]:
            ronda_final[jugador][estadistica] += 1
            ronda_final[jugador]['puntos'] -= 1  
            mvp_porpartida[jugador] -= 1

def calcular_mvp(ronda_final, mvp_porpartida):
    max = -100
    for jugador in mvp_porpartida:
        if(mvp_porpartida[jugador] > max):
            max = mvp_porpartida[jugador]
            j = jugador
    ronda_final[j]['MVPs'] +=1 
        

def inicializar_en0(mvp_porpartida):
    for elem in mvp_porpartida:
        mvp_porpartida[elem] = 0

def imprimir_porronda(elem,mvp_porpartida,ronda):
    print()
    print(f"Ranking ronda {ronda}")
    print(' jugador   kills   asistencias   muertes ')
    print('-----------------------------------------')
    for jugador in elem:
        print(f" {jugador}      {elem[jugador]['kills']}          {elem[jugador]['assists']}         {elem[jugador]['deaths']}\n")
    print('-----------------------------------------')
    print()
   






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
     
        