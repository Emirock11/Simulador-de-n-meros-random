from ResultadosGUI import res5
from Chi_Cuadrada import ventanaChiCuadrada
from Kolmogorov import ventanaKolmogorov

def generadorMultiplicativo(x0, a, m, n, opcion):
    numRand = []
    Semillas = []
    Ri = []

    for i in range(n):
        Semillas.append(x0)
        x1 = (a * x0) % m
        numRand.append(x1)
        Ri.append(x1/m)
        x0 = x1
    if opcion == 0:
        res5(numRand, a, m, Semillas, Ri)
    elif opcion == 1:
        ventanaChiCuadrada(Ri)
    else:
        ventanaKolmogorov(Ri)