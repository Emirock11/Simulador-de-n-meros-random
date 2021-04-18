from ResultadosGUI import res4

def congruencialLinealCombinado(a1, a2, m1, m2, X1, Y1, n):
    Xn = []
    Yn = []
    Wn = []

    for i in range (n):
        if i != 0:
            X1 = a1 * X1 % m1
            Y1 = a2 * Y1 % m2
        W1 = (X1 - Y1) % m2
        Xn.append(X1)
        Yn.append(Y1)
        Wn.append(W1)

    res4(Xn, Yn, Wn)