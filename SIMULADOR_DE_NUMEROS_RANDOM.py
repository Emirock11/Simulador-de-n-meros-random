import tkinter as tk
from PIL import Image, ImageTk
from Tests import basicRules1, basicRules2, basicRules3, basicRules4
from CongruenciaLineal import conguencialLineal
from CongruenciaLinealCombinado import congruencialLinealCombinado
from CongruencialMixto import conguencialMixto
from CuadradosMedios import cuadradosMedios
from GeneradorMultiplicativo import generadorMultiplicativo
from pruebaSimulador import pruebaSimulador


'''
En este archivo se realiza la interfaz de nuestro generador de numeros random

'''
def mostrarValidaciones():
    buttonKolmo.place(relx=0.58, rely=0.63, relwidth=0.3)
    buttonChi.place(relx=0.62, rely=0.5, relwidth=0.22)

def ocultarValidaciones():
    buttonKolmo.place_forget()
    buttonChi.place_forget()

def ocultarCLC():
    seedLabel.place(relx=0.109, rely=0.38, relwidth=0.2)
    multiplierLabel.place(relx=0.088, rely=0.48, relwidth=0.22)
    constantLabel.place(relx=0.062, rely=0.58, relwidth=0.25)
    modLabel.place(relx=0.01, rely=0.68, relwidth=0.3)
    m1Label.place_forget()
    m2Label.place_forget()
    a1Label.place_forget()
    a2Label.place_forget()
    x1Label.place_forget()
    y1Label.place_forget()
    x1Entry.place_forget()
    y1Entry.place_forget()


def mostrarCLC():
    m1Label.place(relx=0.09, rely=0.58, relwidth=0.215)
    m2Label.place(relx=0.09, rely=0.68, relwidth=0.215)
    a1Label.place(relx=0.062, rely=0.38, relwidth=0.24)
    a2Label.place(relx=0.062, rely=0.48, relwidth=0.24)
    x1Label.place(relx=0.53, rely=0.48, relwidth=0.22)
    y1Label.place(relx=0.53, rely=0.58, relwidth=0.22)
    x1Entry.place(relx=0.768, rely=0.48, relwidth=0.15)
    y1Entry.place(relx=0.768, rely=0.58, relwidth=0.15)
    seedLabel.place_forget()
    multiplierLabel.place_forget()
    constantLabel.place_forget()
    modLabel.place_forget()

def resolver(n):
    current = var.get()
    seed = int(seedEntry.get())
    rand = int(randEntry.get())
    if current == "Metodo de los Centros Cuadrados":
        cuadradosMedios(seed,rand)
    elif current == "Generador Multiplicativo":
        multiplier = int(multiplierEntry.get())
        module = int(modEntry.get())
        generadorMultiplicativo(seed, multiplier, module, rand, n)
        
    elif current == "Metodo Congruencial lineal Combinado":
        multiplier = int(multiplierEntry.get())
        constant = int(constantEntry.get())
        module = int(modEntry.get())
        X1 = int(x1Entry.get())
        Y1 = int(y1Entry.get())
        congruencialLinealCombinado(seed, multiplier, constant, module, X1, Y1, rand)
    
    elif current == "Metodo Congruencial Mixto":
        multiplier = int(multiplierEntry.get())
        constant = int(constantEntry.get())
        module = int(modEntry.get())
        conguencialMixto(seed,multiplier,constant, module, rand, n)

    else:
        multiplier = int(multiplierEntry.get())
        constant = int(constantEntry.get())
        module = int(modEntry.get())
        conguencialLineal(seed, multiplier, constant, module, rand, n)
         

def option_changed(*args):
    current = var.get()
    if current == "Metodo de los Centros Cuadrados":
        multiplierEntry.config(state='disabled')
        constantEntry.config(state='disabled')
        modEntry.config(state='disabled')
        multiplierLabel.config(bg='#74d9ee')
        constantLabel.config(bg='#74d9ee')
        modLabel.config(bg='#74d9ee')
        ocultarValidaciones()
        ocultarCLC()
        buttonCalcular.place(relx=0.43, rely = 0.9)
    elif  current == "Metodo Congruencial lineal Combinado":
        multiplierEntry.config(state='normal')
        constantEntry.config(state='normal')
        modEntry.config(state='normal')
        multiplierLabel.config(bg='#74ee7e')
        constantLabel.config(bg='#74ee7e')
        modLabel.config(bg='#74ee7e')
        ocultarValidaciones()
        mostrarCLC()
        buttonCalcular.place(relx=0.43, rely = 0.9)
    elif current == "Generador Multiplicativo":
        multiplierEntry.config(state='normal')
        constantEntry.config(state='disabled')
        modEntry.config(state='normal')
        multiplierLabel.config(bg='#74ee7e')
        constantLabel.config(bg='#74d9ee')
        modLabel.config(bg='#74ee7e')
        mostrarValidaciones()
        ocultarCLC()
    else:
        multiplierEntry.config(state='normal')
        constantEntry.config(state='normal')
        modEntry.config(state='normal')
        multiplierLabel.config(bg='#74ee7e')
        constantLabel.config(bg='#74ee7e')
        modLabel.config(bg='#74ee7e')
        mostrarValidaciones()
        ocultarCLC()

def quitarLabelsErrores():
    strLabel1.place_forget()
    strLabel2.place_forget()
    strLabel3.place_forget()
    strLabel4.place_forget()

def calculateChi():
    calculate(1)

def calculateKol():
    calculate(2)

def calculateRes():
    calculate(0)

def pruebaSim():
    pruebaSimulador()

def calculate(n):
    current = var.get()
    try:
        seed = int(seedEntry.get())
        rand = int(randEntry.get())
        if current == "Metodo de los Centros Cuadrados":
            checker = basicRules1(seed, rand)
        elif current == "Generador Multiplicativo":
            multiplier = int(multiplierEntry.get())
            module = int(modEntry.get())
            checker = basicRules3(seed, rand, multiplier, module)
        elif current == "Metodo Congruencial lineal Combinado":
            multiplier = int(multiplierEntry.get())
            constant = int(constantEntry.get())
            module = int(modEntry.get())
            X1 = int(x1Entry.get())
            Y1 = int(y1Entry.get())
            checker = basicRules4(seed, multiplier, constant, module, X1, Y1, rand)
        else:
            multiplier = int(multiplierEntry.get())
            constant = int(constantEntry.get())
            module = int(modEntry.get())
            checker = basicRules2(seed, rand, multiplier, constant, module)
        
        if checker == 2:
            quitarLabelsErrores()
            strLabel2.place(relx=0, rely=0.8, relwidth=1)
        elif checker == 3:
            quitarLabelsErrores()
            strLabel3.place(relx=0, rely=0.8, relwidth=1)
        elif checker == 4:
            quitarLabelsErrores()
            strLabel4.place(relx=0, rely=0.8, relwidth=1)
        elif checker == 1:
            quitarLabelsErrores()
            resolver(n)
    except:
        strLabel1.place(relx=0, rely=0.8, relwidth=1)

    

TFont = ("Verdana", 15)

listMethods = ["Metodo de los Centros Cuadrados","Metodo Congruencial","Metodo Congruencial Mixto", "Metodo Congruencial lineal Combinado", "Generador Multiplicativo"]

app = tk.Tk()

canvas = tk.Canvas(app, height=400, width=800, bg='#31a5db')
canvas.pack()

mainFrame = tk.Frame(canvas, bg='#2fe7ea')
mainFrame.place(relx=0.05, rely=0, relwidth=0.9, relheight=1)

label = tk.Label(canvas, text="Simulador de Numeros Random", fg='Black', bg='#74d9ee', font=TFont)
label.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.1)

# Frame 1 / Inicio

frame1 = tk.Frame(mainFrame, bg='#74d9ee')
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.9)

# Contenido del frame 1 / Inicio

labelMetodo = tk.Label(frame1, text="Selecciona el metodo a utilizar: ", bg='#74ee7e')
labelMetodo.place(relx=0.075, rely=0.27, relwidth=0.23)

var = tk.StringVar(frame1)
var.set(listMethods[0])
var.trace("w", option_changed)
methodsMenu = tk.OptionMenu(frame1, var, *listMethods)
methodsMenu.config(highlightbackground ='#74d9ee')
methodsMenu.place(relx=0.33, rely=0.25, relwidth=0.37)

seedLabel = tk.Label(frame1, text="Ingresa la semilla (X0 > 0): ", bg='#74ee7e')
seedLabel.place(relx=0.109, rely=0.38, relwidth=0.2)

seedVar = tk.StringVar(frame1)
seedEntry = tk.Entry(frame1, textvariable=seedVar)
seedEntry.place(relx=0.33, rely=0.38, relwidth=0.15)

randLabel = tk.Label(frame1, text="Cantidad de numeros random: ", bg='#74ee7e')
randLabel.place(relx=0.509, rely=0.38, relwidth=0.24)

randVar = tk.StringVar(frame1)
randEntry = tk.Entry(frame1, textvariable=randVar)
randEntry.place(relx=0.768, rely=0.38, relwidth=0.15)

multiplierLabel = tk.Label(frame1, text="Ingresa multiplicador (a > 0): ", bg='#74d9ee')
multiplierLabel.place(relx=0.088, rely=0.48, relwidth=0.22)
multiplierVar = tk.StringVar(frame1)
multiplierEntry = tk.Entry(frame1, textvariable=multiplierVar, state='disabled')
multiplierEntry.place(relx=0.33, rely=0.48, relwidth=0.15)

constantLabel = tk.Label(frame1, text="Ingresa constante aditiva (c > 0): ", bg='#74d9ee')
constantLabel.place(relx=0.062, rely=0.58, relwidth=0.25)
constantVar = tk.StringVar(frame1)
constantEntry = tk.Entry(frame1, textvariable=constantVar, state='disabled')
constantEntry.place(relx=0.33, rely=0.58, relwidth=0.15)

modLabel = tk.Label(frame1, text="Ingresa módulo (m > Xi, m > a, m > c): ", bg='#74d9ee')
modLabel.place(relx=0.01, rely=0.68, relwidth=0.3)
modVar = tk.StringVar(frame1)
modEntry = tk.Entry(frame1, textvariable=modVar, state='disabled')
modEntry.place(relx=0.33, rely=0.68, relwidth=0.15)

strLabel1 = tk.Label(frame1, text="Falta completar los datos o alguno de los datos ingresados contiene un caracter. Se deben de ingresar numeros solamente.", fg='#ff2828', bg='#74d9ee')

strLabel2 = tk.Label(frame1, text="La semilla, multiplicador y la constante aditiva deben ser mayores a cero.", fg='#ff2828', bg='#74d9ee')

strLabel3 = tk.Label(frame1, text="El módulo debe ser mayor a la semilla, multimplicador y la constante.", fg='#ff2828', bg='#74d9ee')

strLabel4 = tk.Label(frame1, text="La cantidad de números random debe ser mayor a 0.", fg='#ff2828', bg='#74d9ee')

quitarLabelsErrores()

buttonChi = tk.Button(frame1, text="Validar con Chi-Cuadrada", command=calculateChi)
buttonChi.place_forget()

buttonKolmo = tk.Button(frame1, text="Validar con Kolmogorov-Smirnov", command=calculateKol)
buttonKolmo.place_forget()

buttonCalcular = tk.Button(frame1, text="Calcular numeros random", command=calculateRes)
buttonCalcular.place(relx=0.4, rely = 0.9)

m1Label = tk.Label(frame1, text="Ingresa módulo 1 (m1 > a1): ", bg='#74ee7e')
m2Label = tk.Label(frame1, text="Ingresa módulo 2 (m2 > a2): ", bg='#74ee7e')
a1Label = tk.Label(frame1, text="Ingresa multiplicador 1 (a1 > 0): ", bg='#74ee7e')
a2Label = tk.Label(frame1, text="Ingresa multiplicador 2 (a2 > 0): ", bg='#74ee7e')
x1Label = tk.Label(frame1, text="Ingresa semilla 'X1' (X1 > 0): ", bg='#74ee7e')
y1Label = tk.Label(frame1, text="Ingresa semilla 'Y1' (Y1 > 0): ", bg='#74ee7e')
x1Var = tk.StringVar(frame1)
x1Entry = tk.Entry(frame1, textvariable=x1Var)
y1Var = tk.StringVar(frame1)
y1Entry = tk.Entry(frame1, textvariable=y1Var)

# Contenido del frame 1 / Fin

# Frame 1 / Fin

frame2 = tk.Frame(mainFrame, bg='#74d9ee')
frame2.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

button = tk.Button(frame2, text="Prueba del Simulador", command=pruebaSimulador)
button.place(relx=0.42, rely=0.2)


app.mainloop()