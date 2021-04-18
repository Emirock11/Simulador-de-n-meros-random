from ResultadosGUI import res2
from Chi_Cuadrada import ventanaChiCuadrada
from Kolmogorov import ventanaKolmogorov

def conguencialLineal(x0, a, c, m, n, opcion):
    numRand = []
    Semillas = []
    Ri = []
    
    for i in range(n):
        Semillas.append(x0)
        x1 = (a * x0 + c) % m
        numRand.append(x1)
        Ri.append(x1/m)
        x0 = x1
    if opcion == 0:
        res2(numRand, m, c, a, Semillas, Ri)
    elif opcion == 1:
        ventanaChiCuadrada(Ri)
    else:
        ventanaKolmogorov(Ri)