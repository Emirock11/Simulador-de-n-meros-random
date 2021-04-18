
'''
    Errores:
        2: La semilla, multiplicador y la constante aditiva deben ser mayores a cero.
        3: El módulo debe ser mayor a la semilla, multimplicador y la constante. 
        4: La cantidad de números randoms debe ser mayor a 0.
    El 1 es que pasó con éxito todas las pruebas
'''

def basicRules1(seed, rand):

    if seed < 1 :
        checker = 2
    elif rand < 1:
        checker = 4
    else:
        checker = 1
    return checker

def basicRules2(seed, rand, multiplier, constant, module):

    if (seed + multiplier + constant) > 2:
        if module > seed and module > multiplier and module > constant:
            if rand > 0:
                checker = 1
            else:
                checker = 4
        else:
             checker = 3
    else: 
        checker = 2
    print("Checker: ",checker)
    return checker

def basicRules3(seed, rand, multiplier, module):

    if (seed + multiplier) > 1:
        if module > seed and module > multiplier:
            if rand > 0:
                checker = 1
            else:
                checker = 4
        else:
             checker = 3
    else: 
        checker = 2
    return checker

def basicRules4(a1, a2, m1, m2, x1, y1, nR):

    if (a1 + a2) > 1 and (x1 + y1) > 1:
        if m1 > a1 and m2 > a2:
            if nR > 0:
                checker = 1
            else:
                checker = 4
        else:
            checker = 3
    else: 
        checker = 2
    return checker