import tkinter as tk
from PIL import Image, ImageTk
from CongruenciaLineal import conguencialLineal
from CongruenciaLinealCombinado import congruencialLinealCombinado
from CongruencialMixto import conguencialMixto
from CuadradosMedios import cuadradosMedios
from GeneradorMultiplicativo import generadorMultiplicativo

def pruebaSimulador():
    seed = 10
    rand = 10
    multiplier = 1
    constant = 7
    module = 12
    m1 = 5
    m2 = 7
    a1 = 3
    a2 = 5
    X1 = 1
    Y1 = 3
    n = 0
    
    def op1():
        cuadradosMedios(3547,rand)
    def op2():
        conguencialLineal(seed, multiplier, constant, module, rand, n)
    def op3():
        conguencialMixto(37,7,29, 100, rand, n)
    def op4():
        congruencialLinealCombinado(a1, a2, m1, m2, X1, Y1, rand)
    def op5():
        generadorMultiplicativo(37, 7, 100, rand, n)

    app = tk.Tk()

    canvas = tk.Canvas(app, height=300, width=400, bg='#31a5db')
    canvas.pack()

    mainFrame = tk.Frame(canvas, bg='#2fe7ea')
    mainFrame.place(relx=0.05, rely=0, relwidth=0.9, relheight=1)

    TFont = ("Verdana", 15)

    # Frame 1 / Inicio

    frame1 = tk.Frame(mainFrame, bg='#74d9ee')
    frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(canvas, text="Prueba del Simulador", fg='Black', bg='#74d9ee', font=TFont)
    label.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    p1 = tk.Button(frame1, text="Metodo de los Centros Cuadrados", command=op1)
    p1.place(relx=0.25, rely = 0.25)

    p2 = tk.Button(frame1, text="Metodo Congruencial", command=op2)
    p2.place(relx=0.34, rely = 0.4)

    p3 = tk.Button(frame1, text="Metodo Congruencial Mixto", command=op3)
    p3.place(relx=0.29, rely = 0.55)

    p4 = tk.Button(frame1, text="Metodo Congruencial lineal Combinado", command=op4)
    p4.place(relx=0.21, rely = 0.7)

    p5 = tk.Button(frame1, text="Generador Multiplicativo", command=op5)
    p5.place(relx=0.32, rely = 0.85)

    
