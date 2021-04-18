from ResultadosGUI import res3
from Chi_Cuadrada import ventanaChiCuadrada
from Kolmogorov import ventanaKolmogorov

# Identificar si dos numeros son primos relativos
def primosRelativos(x,y):
    # Clasificamos el número mayor y el menor
    a = min(x,y)
    b = max(x,y)
    div = 2

    while(div <= a):
        # Si el residuo de la división de a y b entre div es igual a cero...
        if(a % div == 0) and (b % div == 0):
            # No son primos relativos
            return False
        div += 1
    return True

# Identificar si un numero es primo
def esPrimo(n):
    contador = 0

    for i in range(1, n+1):
        if n % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

# Obtener un numero primo divisor de un numero
def numPrimoDivX(x):
    div = 2

    while(div <= x):
        if esPrimo(div) and x % div == 0:
            return div
        div += 1

# Si q es un numero primo que divide a m; entonces, q divide a (a-1)
def segundaComprobacion(m, a):
    numPrimo = numPrimoDivX(m)
    if (m % numPrimo == 0) and ((a - 1) % numPrimo == 0):
        return True
    else:
        return False

# Si 4 divide a m; entonces, 4 divide a (a-1).
def terceraComprobacion(m, a):
    if (m % 4 == 0) and ((a - 1) % 4 == 0):
        return True
    else:
        return False

# Ver si el generador congruencial mixto tiene periodo completo...
def hullDobell(c, m, a):
    if primosRelativos(c, m) and segundaComprobacion(m, a) and terceraComprobacion(m, a):
        return True
    else:
        return False

def conguencialMixto(x0, a, c, m, n, opcion):
    numRand = []
    Semillas = []
    Ri = []
    periodoCompleto = hullDobell(c, m, a)

    for i in range(n):
        Semillas.append(x0)
        x1 = (a * x0 + c) % m
        numRand.append(x1)
        Ri.append(x1/m)
        x0 = x1
    if opcion == 0:
        res3(numRand, periodoCompleto, a, c, m, Semillas, Ri)
    elif opcion == 1:
        ventanaChiCuadrada(Ri)
    else:
        ventanaKolmogorov(Ri)